/** Test the distributable tarball, not a checkout masquerading as an install. */
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const npm = process.platform === 'win32' ? 'npm.cmd' : 'npm';

test('npm tarball installs offline through its public bin and preserves every Skill byte', async () => {
  const temporary = await fs.mkdtemp(path.join(os.tmpdir(), 'research npm 空格 '));
  try {
    const env = { ...process.env, npm_config_cache: path.join(temporary, 'cache'), npm_config_update_notifier: 'false' };
    const run = (args, cwd = root) => {
      const result = spawnSync(npm, args, { cwd, env, encoding: 'utf8', timeout: 120000 });
      assert.equal(result.status, 0, `${result.error || ''}\n${result.stderr}\n${result.stdout}`);
      return result.stdout;
    };
    const metadata = JSON.parse(run(['pack', '--ignore-scripts', '--json', '--pack-destination', temporary]))[0];
    assert.ok(metadata.files.some(f => f.path === 'bin/install.mjs'));
    assert.ok(!metadata.files.some(f => /^(docs|tools|scripts)\//.test(f.path)), 'Only runtime content belongs in the npm package');
    const skill = 'research-english-academic-paper-writing-guide';
    const archive = path.join(temporary, metadata.filename);
    const project = path.join(temporary, 'consumer');
    await fs.mkdir(project);
    await fs.writeFile(path.join(project, 'package.json'), '{"name":"isolated-consumer","private":true}');
    run(['install', '--offline', '--ignore-scripts', '--no-audit', '--no-fund', archive], project);
    const target = path.join(temporary, 'installed skills');
    const execute = (...args) => run(['exec', '--offline', '--', 'research-writing-skill-install', '--target', target, ...args], project);
    const installed = JSON.parse(execute());
    assert.equal(installed.action, 'installed');
    assert.equal(JSON.parse(execute()).action, 'unchanged');
    assert.equal(JSON.parse(execute('--verify')).action, 'verified');
    const files = metadata.files.filter(f => f.path.startsWith(`skills/${skill}/`));
    const tracked = spawnSync('git', ['ls-files', '-z', `skills/${skill}`], { cwd: root, encoding: 'utf8' });
    assert.equal(tracked.status, 0, tracked.stderr);
    assert.deepEqual(files.map(f => f.path).sort(), tracked.stdout.split('\0').filter(Boolean).sort(), 'Tarball must contain the complete tracked Skill path set');
    assert.equal(installed.files, files.length);
    for (const file of files) {
      const relative = file.path.slice(`skills/${skill}/`.length);
      assert.deepEqual(await fs.readFile(path.join(target, skill, relative)), await fs.readFile(path.join(root, file.path)), relative);
    }
    for (const entry of ['.agents/plugins/marketplace.json', '.claude-plugin/plugin.json', 'plugin.json']) {
      assert.ok(metadata.files.some(f => f.path === entry), `Missing plugin file ${entry}`);
    }
  } finally {
    await fs.rm(temporary, { recursive: true, force: true });
  }
});
