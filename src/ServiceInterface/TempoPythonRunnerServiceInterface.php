<?php

declare(strict_types=1);

namespace App\Temporaring\ServiceInterface;

use App\Temporaring\DTO\TempoRunResultDTO;

/**
 * Defines the deterministic PHP-to-Python hypothesis execution boundary for Temporaring.
 */
interface TempoPythonRunnerServiceInterface
{
    /** Executes one immutable System Tempo hypothesis through the Python compute plane. */
    public function run(string $hypothesisPath): TempoRunResultDTO;
}
