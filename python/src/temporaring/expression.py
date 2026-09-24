"""Safe deterministic parser for System Tempo symbolic expressions."""

from __future__ import annotations

import ast
from collections.abc import Mapping
from typing import Any

import sympy


_MAX_EXPRESSION_LENGTH = 4096
_MAX_AST_NODES = 256

_FUNCTIONS: Mapping[str, Any] = {
    "sin": sympy.sin,
    "cos": sympy.cos,
    "tan": sympy.tan,
    "asin": sympy.asin,
    "acos": sympy.acos,
    "atan": sympy.atan,
    "sinh": sympy.sinh,
    "cosh": sympy.cosh,
    "tanh": sympy.tanh,
    "exp": sympy.exp,
    "log": sympy.log,
    "sqrt": getattr(sympy, "sqrt"),
}

_CONSTANTS: Mapping[str, Any] = {
    "E": getattr(sympy, "E"),
    "pi": getattr(sympy, "pi"),
}


def parse_expression(expression: str, symbols: Mapping[str, sympy.Symbol]) -> Any:
    """Parse the supported expression grammar without eval-backed SymPy parsing."""

    if len(expression) > _MAX_EXPRESSION_LENGTH:
        raise ValueError("expression exceeds the maximum supported length")

    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exception:
        raise ValueError("expression is not valid arithmetic syntax") from exception

    if sum(1 for _ in ast.walk(tree)) > _MAX_AST_NODES:
        raise ValueError("expression exceeds the maximum supported complexity")

    return _build_expression(tree.body, symbols)


def _build_expression(node: ast.AST, symbols: Mapping[str, sympy.Symbol]) -> Any:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("only real numeric literals are allowed")
        return sympy.Integer(node.value) if isinstance(node.value, int) else sympy.Float(node.value)

    if isinstance(node, ast.Name):
        if node.id in symbols:
            return symbols[node.id]
        if node.id in _CONSTANTS:
            return _CONSTANTS[node.id]
        raise ValueError(f"undeclared symbol or unsupported constant: {node.id}")

    if isinstance(node, ast.UnaryOp):
        operand = _build_expression(node.operand, symbols)
        if isinstance(node.op, ast.UAdd):
            return operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError("unsupported unary operator")

    if isinstance(node, ast.BinOp):
        left = _build_expression(node.left, symbols)
        right = _build_expression(node.right, symbols)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            return left**right
        raise ValueError("unsupported binary operator")

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("only direct calls to supported mathematical functions are allowed")
        function = _FUNCTIONS.get(node.func.id)
        if function is None:
            raise ValueError(f"unsupported mathematical function: {node.func.id}")
        if node.keywords:
            raise ValueError("mathematical function keyword arguments are not allowed")
        arguments = [_build_expression(argument, symbols) for argument in node.args]
        if len(arguments) != 1:
            raise ValueError(f"mathematical function {node.func.id} requires exactly one argument")
        return function(arguments[0])

    raise ValueError(f"unsupported expression syntax: {type(node).__name__}")
