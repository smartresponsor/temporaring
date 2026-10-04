<?php

declare(strict_types=1);

namespace App\Temporaring\Tests\Unit;

use App\Temporaring\Command\TempoHypothesisRunCommand;
use App\Temporaring\DTO\TempoRunResultDTO;
use App\Temporaring\Service\TempoPythonRunnerService;
use App\Temporaring\ServiceInterface\TempoPythonRunnerServiceInterface;
use PHPUnit\Framework\TestCase;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Tester\CommandTester;

final class TempoRuntimeCoverageTest extends TestCase
{
    public function testCommandRunsTypedRunner(): void
    {
        $runner = $this->createMock(TempoPythonRunnerServiceInterface::class);
        $runner->expects(self::once())->method('run')->with('fixture.json')
            ->willReturn(new TempoRunResultDTO([
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
            ], '{"status":"falsified"}'));
        $tester = new CommandTester(new TempoHypothesisRunCommand($runner));
        self::assertSame(Command::SUCCESS, $tester->execute(['hypothesis' => 'fixture.json']));
        self::assertStringContainsString('falsified', $tester->getDisplay());
    }

    public function testCommandRejectsEmptyHypothesis(): void
    {
        $runner = $this->createMock(TempoPythonRunnerServiceInterface::class);
        $runner->expects(self::never())->method('run');
        $tester = new CommandTester(new TempoHypothesisRunCommand($runner));
        self::assertSame(Command::INVALID, $tester->execute(['hypothesis' => '']));
    }

    public function testRunnerExecutesCanonicalFixture(): void
    {
        $root = dirname(__DIR__, 2);
        $python = implode(DIRECTORY_SEPARATOR, [
            $root,
            'python',
            '.venv',
            PHP_OS_FAMILY === 'Windows' ? 'Scripts' : 'bin',
            PHP_OS_FAMILY === 'Windows' ? 'python.exe' : 'python',
        ]);
        $runner = new TempoPythonRunnerService($root, $python);
        $result = $runner->run($root.'\\research\\hypothesis\\common-positive.json');
        self::assertSame('pure_time_reparameterization', $result->classification());
        self::assertSame('falsified', $result->payload['status']);
    }

    public function testRunnerRejectsMissingHypothesis(): void
    {
        $runner = new TempoPythonRunnerService(dirname(__DIR__, 2));
        $this->expectException(\RuntimeException::class);
        $this->expectExceptionMessage('Hypothesis file does not exist');
        $runner->run('does-not-exist.json');
    }
}
