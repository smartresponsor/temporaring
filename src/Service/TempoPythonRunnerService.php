<?php

declare(strict_types=1);

namespace App\Temporaring\Service;

use App\Temporaring\DTO\TempoRunResultDTO;
use App\Temporaring\ServiceInterface\TempoPythonRunnerServiceInterface;
use Symfony\Component\Process\Process;

/**
 * Executes the isolated Python classifier and validates its result at the PHP boundary.
 */
final readonly class TempoPythonRunnerService implements TempoPythonRunnerServiceInterface
{
    public function __construct(
        private string $projectDir,
        private string $pythonExecutable = 'python',
    ) {
    }

    /**
     * Runs one hypothesis file and returns a validated immutable scientific result envelope.
     */
    public function run(string $hypothesisPath): TempoRunResultDTO
    {
        $resolvedPath = realpath($hypothesisPath);
        if (false === $resolvedPath || !is_file($resolvedPath)) {
            throw new \RuntimeException(sprintf('Hypothesis file does not exist: %s', $hypothesisPath));
        }

        $process = new Process([
            $this->pythonExecutable,
            '-m',
            'temporaring.runner',
            '--input',
            $resolvedPath,
        ], $this->projectDir, [
            'PYTHONPATH' => $this->projectDir.DIRECTORY_SEPARATOR.'python'.DIRECTORY_SEPARATOR.'src',
        ]);
        $process->setTimeout(60.0);
        $process->mustRun();

        $rawOutput = trim($process->getOutput());

        try {
            $payload = json_decode($rawOutput, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new \RuntimeException('Python compute plane returned invalid JSON.', 0, $exception);
        }

        if (!is_array($payload)) {
            throw new \RuntimeException('Python compute plane returned a non-object JSON payload.');
        }

        return new TempoRunResultDTO($payload, $rawOutput);
    }
}
