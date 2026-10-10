import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const bin = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../bin/install.mjs');
async function fixture() {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'skill installer 空格 '));
  const source = path.join(root, 'source'), skill = path.join(source, 'skills', 'read-example');
  await fs.mkdir(path.join(skill, 'assets', '.hidden'), { recursive: true });
  await fs.writeFile(path.join(source, 'package.json'), JSON.stringify({ name: 'test-fixture', version: '1.0.0' }));
  await fs.writeFile(path.join(skill, 'SKILL.md'), '---\r\nname: read-example\r\ndescription: Read original fixtures.\r\n---\r\n全书原文\r\n');
  await fs.writeFile(path.join(skill, 'assets', '.hidden', 'original.bin'), Buffer.from([0, 255, 17, 10, 13, 128]));
  const parent = path.join(root, 'installed skills');
  const run = (...options) => spawnSync(process.execPath, [bin, '--source', source, '--target', parent, ...options], { encoding: 'utf8' });
  return { root, source, skill, parent, run };
}

test('complete binary and CRLF copying, idempotency, verification, and dry run', async () => {
  const f = await fixture();
  try {
    assert.equal(f.run('--dry-run').status, 0);
    await assert.rejects(fs.stat(f.parent));
    const install = f.run(); assert.equal(install.status, 0, install.stderr);
    const dest = path.join(f.parent, 'read-example');
    assert.deepEqual(await fs.readFile(path.join(dest, 'SKILL.md')), await fs.readFile(path.join(f.skill, 'SKILL.md')));
    assert.deepEqual(await fs.readFile(path.join(dest, 'assets', '.hidden', 'original.bin')), Buffer.from([0, 255, 17, 10, 13, 128]));
    assert.equal(JSON.parse(f.run().stdout).action, 'unchanged');
    assert.equal(f.run('--verify').status, 0);
    await fs.writeFile(path.join(dest, 'personal-note.md'), 'local note');
    assert.notEqual(f.run('--verify').status, 0);
    await fs.appendFile(path.join(f.skill, 'SKILL.md'), '\nNew version\n');
    const refused = f.run('--upgrade'); assert.notEqual(refused.status, 0);
    assert.equal(await fs.readFile(path.join(dest, 'personal-note.md'), 'utf8'), 'local note');
    assert.ok(!await fs.readdir(f.parent).then(names => names.some(n => n.includes('-stage-'))));
  } finally { await fs.rm(f.root, { recursive: true, force: true }); }
});

test('a clean managed upgrade retains the old complete bytes and receipt', async () => {
  const f = await fixture();
  try {
    assert.equal(f.run().status, 0);
    const original = await fs.readFile(path.join(f.skill, 'SKILL.md'));
    await fs.appendFile(path.join(f.skill, 'SKILL.md'), '\nAdditional source; no abridgment.\n');
    assert.notEqual(f.run().status, 0);
    const upgrade = f.run('--upgrade'); assert.equal(upgrade.status, 0, upgrade.stderr);
    const report = JSON.parse(upgrade.stdout);
    assert.deepEqual(await fs.readFile(path.join(report.backup, 'skill', 'SKILL.md')), original);
    assert.equal(JSON.parse(await fs.readFile(path.join(report.backup, 'receipt.json'), 'utf8')).version, '1.0.0');
    assert.equal(f.run('--verify').status, 0);
  } finally { await fs.rm(f.root, { recursive: true, force: true }); }
});

test('unmanaged files and symlink targets are refused without mutation', async () => {
  const f = await fixture();
  try {
    const dest = path.join(f.parent, 'read-example');
    await fs.mkdir(dest, { recursive: true });
    await fs.writeFile(path.join(dest, 'SKILL.md'), 'personal content');
    assert.notEqual(f.run('--upgrade').status, 0);
    assert.equal(await fs.readFile(path.join(dest, 'SKILL.md'), 'utf8'), 'personal content');
    const link = path.join(f.root, 'linked-target');
    await fs.symlink(f.parent, link, 'dir');
    const unsafe = spawnSync(process.execPath, [bin, '--source', f.source, '--target', link], { encoding: 'utf8' });
    assert.notEqual(unsafe.status, 0);
    assert.match(unsafe.stderr, /Symlink/);
  } finally { await fs.rm(f.root, { recursive: true, force: true }); }
});
