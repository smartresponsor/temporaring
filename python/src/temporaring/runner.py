"""CLI entrypoint for deterministic System Tempo hypothesis classification."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import sympy

from temporaring.contract import TempoHypothesis
from temporaring.validator.reparameterization import classify_reparameterization


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    raw = args.input.read_bytes()
    payload = json.loads(raw)
    hypothesis = TempoHypothesis.model_validate(payload)
    classification = classify_reparameterization(hypothesis)

    result = {
        "schema_version": "1.0",
        "hypothesis_id": hypothesis.hypothesis_id,
        "status": classification.status,
        "classification": classification.classification,
        "reason": classification.reason,
        "transformation": classification.transformation,
        "invariants": list(classification.invariants),
        "provenance": {
            "input_sha256": hashlib.sha256(raw).hexdigest(),
            "python_version": platform.python_version(),
            "sympy_version": sympy.__version__,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
