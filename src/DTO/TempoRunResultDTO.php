<?php

declare(strict_types=1);

namespace App\Temporaring\DTO;

/**
 * Validates and exposes the stable result envelope returned by the Python compute plane.
 */
final readonly class TempoRunResultDTO
{
    /** @param array<string, mixed> $payload */
    public function __construct(
        public array $payload,
        public string $rawOutput,
    ) {
        foreach (['hypothesis_id', 'status', 'classification', 'reason'] as $field) {
            $this->requireNonEmptyString($field);
        }

        if ('1.0' !== $this->requireNonEmptyString('schema_version')) {
            throw new \UnexpectedValueException('Python compute plane returned an unsupported result schema_version.');
        }

        if (array_key_exists('transformation', $this->payload)
            && null !== $this->payload['transformation']
            && !is_string($this->payload['transformation'])) {
            throw new \UnexpectedValueException('Python compute plane returned an invalid transformation field.');
        }

        $invariants = $this->payload['invariants'] ?? null;
        if (!is_array($invariants)
            || !array_is_list($invariants)
            || array_any($invariants, static fn (mixed $invariant): bool => !is_string($invariant) || '' === $invariant)) {
            throw new \UnexpectedValueException('Python compute plane returned an invalid invariants field.');
        }

        $provenance = $this->payload['provenance'] ?? null;
        if (!is_array($provenance)) {
            throw new \UnexpectedValueException('Python compute plane returned an invalid provenance field.');
        }

        foreach (['input_sha256', 'python_version', 'sympy_version'] as $field) {
            $value = $provenance[$field] ?? null;
            if (!is_string($value) || '' === $value) {
                throw new \UnexpectedValueException(sprintf('Python compute plane result provenance is missing a valid %s field.', $field));
            }
        }
    }

    /**
     * Returns the validated scientific classification from the immutable result payload.
     */
    public function classification(): string
    {
        return $this->requireNonEmptyString('classification');
    }

    private function requireNonEmptyString(string $field): string
    {
        $value = $this->payload[$field] ?? null;
        if (!is_string($value) || '' === $value) {
            throw new \UnexpectedValueException(sprintf('Python compute plane result is missing a valid %s field.', $field));
        }

        return $value;
    }
}
