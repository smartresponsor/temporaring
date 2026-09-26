<?php

declare(strict_types=1);

namespace App\Temporaring\Tests\Unit\DTO;

use App\Temporaring\DTO\TempoRunResultDTO;
use PHPUnit\Framework\TestCase;

final class TempoRunResultDTOTest extends TestCase
{
    public function testClassificationReturnsCanonicalPayloadValue(): void
    {
        $result = new TempoRunResultDTO(
            $this->validPayload(),
            '{"classification":"pure_time_reparameterization"}',
        );

        self::assertSame('pure_time_reparameterization', $result->classification());
    }

    public function testResultRejectsMissingClassification(): void
    {
        $payload = $this->validPayload();
        unset($payload['classification']);

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('missing a valid classification field');

        new TempoRunResultDTO($payload, '{}');
    }

    public function testResultRejectsNonStringClassification(): void
    {
        $payload = $this->validPayload();
        $payload['classification'] = 42;

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('missing a valid classification field');

        new TempoRunResultDTO($payload, '{"classification":42}');
    }

    public function testResultRejectsIncompleteProvenance(): void
    {
        $payload = $this->validPayload();
        $payload['provenance'] = ['input_sha256' => 'abc'];

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('provenance is missing a valid python_version field');

        new TempoRunResultDTO($payload, '{}');
    }

    public function testResultRejectsUnsupportedSchemaVersion(): void
    {
        $payload = $this->validPayload();
        $payload['schema_version'] = '2.0';

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('unsupported result schema_version');

        new TempoRunResultDTO($payload, '{}');
    }

    public function testResultRejectsInvalidTransformation(): void
    {
        $payload = $this->validPayload();
        $payload['transformation'] = ['not-a-string'];

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('invalid transformation field');

        new TempoRunResultDTO($payload, '{}');
    }

    public function testResultRejectsInvalidInvariants(): void
    {
        $payload = $this->validPayload();
        $payload['invariants'] = [''];

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('invalid invariants field');

        new TempoRunResultDTO($payload, '{}');
    }

    public function testResultRejectsNonObjectProvenance(): void
    {
        $payload = $this->validPayload();
        $payload['provenance'] = 'not-an-object';

        $this->expectException(\UnexpectedValueException::class);
        $this->expectExceptionMessage('invalid provenance field');

        new TempoRunResultDTO($payload, '{}');
    }

    /** @return array<string, mixed> */
    private function validPayload(): array
    {
        return [
            'schema_version' => '1.0',
            'hypothesis_id' => 'tempo-test-001',
            'status' => 'falsified',
            'classification' => 'pure_time_reparameterization',
            'reason' => 'test fixture',
            'transformation' => 'd_tau = (2) * dt',
            'invariants' => ['state_space_orbits'],
            'provenance' => [
                'input_sha256' => str_repeat('a', 64),
                'python_version' => '3.12.1',
                'sympy_version' => '1.14.0',
            ],
        ];
    }
}
