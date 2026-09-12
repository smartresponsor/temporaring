<?php

declare(strict_types=1);

namespace App\Temporaring\Command;

use App\Temporaring\ServiceInterface\TempoPythonRunnerServiceInterface;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(
    name: 'tempo:hypothesis:run',
    description: 'Classify one System Tempo hypothesis through the deterministic Python compute plane.',
)]
final class TempoHypothesisRunCommand extends Command
{
    public function __construct(
        private readonly TempoPythonRunnerServiceInterface $runner,
    ) {
        parent::__construct();
    }

    protected function configure(): void
    {
        $this->addArgument('hypothesis', InputArgument::REQUIRED, 'Path to a hypothesis JSON specification.');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $path = $input->getArgument('hypothesis');
        if (!is_string($path) || '' === $path) {
            return Command::INVALID;
        }

        $result = $this->runner->run($path);
        $output->writeln($result->rawOutput);

        return Command::SUCCESS;
    }
}
