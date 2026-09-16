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
            ['classification' => 'pure_time_reparameterization'],
            '{"classification":"pure_time_reparameterization"}',
        );

        self::assertSame('pure_time_reparameterization', $result->classification());
    }

    public function testClassificationFallsBackToUnknownForMissingValue(): void
    {
        $result = new TempoRunResultDTO([], '{}');

        self::assertSame('unknown', $result->classification());
    }

    public function testClassificationFallsBackToUnknownForNonStringValue(): void
    {
        $result = new TempoRunResultDTO(['classification' => 42], '{"classification":42}');

        self::assertSame('unknown', $result->classification());
    }
}
