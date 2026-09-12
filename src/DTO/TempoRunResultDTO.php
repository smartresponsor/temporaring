<?php

declare(strict_types=1);

namespace App\Temporaring\DTO;

final readonly class TempoRunResultDTO
{
    /** @param array<string, mixed> $payload */
    public function __construct(
        public array $payload,
        public string $rawOutput,
    ) {
    }

    public function classification(): string
    {
        $classification = $this->payload['classification'] ?? null;

        return is_string($classification) ? $classification : 'unknown';
    }
}
