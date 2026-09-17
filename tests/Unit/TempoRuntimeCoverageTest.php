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
            ->willReturn(new TempoRunResultDTO(['classification' => 'pure_time_reparameterization'], '{"status":"falsified"}'));
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
        $python = $root.'\\python\\.venv\\Scripts\\python.exe';
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
