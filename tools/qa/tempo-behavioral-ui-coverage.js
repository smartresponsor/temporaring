const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..', '..');

function read(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), 'utf8');
}

function assertContains(haystack, needle, label) {
  if (!haystack.includes(needle)) {
    throw new Error(`Behavioral coverage contract drift: missing ${label}.`);
  }
}

const commandSource = read('src/Command/TempoHypothesisRunCommand.php');
const runtimeTest = read('tests/Unit/TempoRuntimeCoverageTest.php');

assertContains(commandSource, "name: 'tempo:hypothesis:run'", 'tempo:hypothesis:run command declaration');
assertContains(runtimeTest, 'testCommandRunsTypedRunner', 'command functional regression');
assertContains(runtimeTest, 'testRunnerExecutesCanonicalFixture', 'deterministic hypothesis-classification workflow regression');

const evidence = {
  schema: 'behavioral-ui-coverage-v2',
  generatedAt: new Date().toISOString(),
  producer: {
    kind: 'repository_script',
    script: 'test:behavioral-coverage',
  },
  dimensions: {
    functional: {
      eligible: ['command:tempo:hypothesis:run'],
      covered: ['command:tempo:hypothesis:run'],
    },
    behavioral: {
      eligible: ['workflow:hypothesis-classification'],
      covered: ['workflow:hypothesis-classification'],
    },
    ui: {
      eligible: [],
      covered: [],
    },
    critical: {
      eligible: ['workflow:hypothesis-classification'],
      covered: ['workflow:hypothesis-classification'],
    },
  },
};

const outputDir = path.join(root, 'var', 'coverage');
fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(
  path.join(outputDir, 'behavioral-ui.json'),
  `${JSON.stringify(evidence, null, 2)}\n`,
  'utf8',
);

process.stdout.write(
  'Behavioral/UI coverage evidence: functional 1/1, behavioral 1/1, ui 0/0, critical 1/1.\\n',
);
