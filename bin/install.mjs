#!/usr/bin/env node
/** Offline, complete-file Agent Skill installer. No dependencies or network calls. */
import fs from 'node:fs/promises';
import { createReadStream } from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { createHash, randomBytes } from 'node:crypto';
import { fileURLToPath } from 'node:url';

const packageRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const agentPaths = {
  codex: ['.agents/skills', '.agents/skills'],
  'claude-code': ['.claude/skills', '.claude/skills'],
  'gemini-cli': ['.agents/skills', '.gemini/skills'],
  'github-copilot': ['.agents/skills', '.copilot/skills'],
  cursor: ['.cursor/skills', '.cursor/skills'],
  generic: ['.agents/skills', '.agents/skills'],
};
const receiptSchema = 'complete-skill-installation/1';

function parse(argv) {
  const args = { agent: 'codex', project: process.cwd() };
  const values = new Set(['agent', 'project', 'target', 'skill', 'source']);
  const flags = new Set(['global', 'upgrade', 'dry-run', 'verify', 'list', 'help']);
  for (let i = 0; i < argv.length; i++) {
    const key = argv[i].replace(/^--/, '');
    if (!argv[i].startsWith('--')) throw new Error(`Unexpected argument: ${argv[i]}`);
    if (values.has(key)) {
      if (!argv[i + 1] || argv[i + 1].startsWith('--')) throw new Error(`Missing --${key} value`);
      args[key] = argv[++i];
    } else if (flags.has(key)) args[key] = true;
    else throw new Error(`Unknown option: --${key}`);
  }
  if (!agentPaths[args.agent]) throw new Error(`Unsupported agent; use ${Object.keys(agentPaths).join(', ')}, or --target`);
  if (args.global && argv.includes('--project')) throw new Error('--global and --project are mutually exclusive');
  if (args.target && args.global) throw new Error('--target and --global are mutually exclusive');
  return args;
}

async function exists(p) {
  try { await fs.lstat(p); return true; } catch (e) { if (e.code === 'ENOENT') return false; throw e; }
}

async function noSymlinkParents(p) {
  let current = path.resolve(p);
  while (true) {
    if (await exists(current)) {
      if ((await fs.lstat(current)).isSymbolicLink()) throw new Error(`Symlink path refused: ${current}`);
    }
    const parent = path.dirname(current);
    if (parent === current) break;
    current = parent;
  }
}

async function hashFile(p) {
  const hash = createHash('sha256');
  for await (const data of createReadStream(p)) hash.update(data);
  return hash.digest('hex');
}

async function walk(root, prefix = '') {
  const out = [];
  for (const entry of (await fs.readdir(path.join(root, prefix), { withFileTypes: true })).sort((a, b) => a.name.localeCompare(b.name))) {
    const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
    // Python's runtime caches are generated files; never exclude original assets.
    if (!rel.startsWith('assets/') && (entry.name === '__pycache__' || entry.name.endsWith('.pyc'))) continue;
    if (entry.isSymbolicLink()) throw new Error(`Source/installation symlink refused: ${rel}`);
    if (entry.isDirectory()) out.push(...await walk(root, rel));
    else if (entry.isFile()) out.push(rel);
    else throw new Error(`Unsupported filesystem entry: ${rel}`);
  }
  return out;
}

async function snapshot(root) {
  const files = Object.create(null);
  for (const rel of await walk(root)) {
    const p = path.join(root, rel), stat = await fs.stat(p);
    files[rel] = { size: stat.size, sha256: await hashFile(p) };
  }
  return files;
}

function same(a, b) {
  const ka = Object.keys(a).sort(), kb = Object.keys(b).sort();
  return ka.length === kb.length && ka.every((k, i) => k === kb[i] && a[k].size === b[k].size && a[k].sha256 === b[k].sha256);
}

async function atomicJson(p, data) {
  const temporary = `${p}.${randomBytes(6).toString('hex')}.tmp`;
  await fs.writeFile(temporary, JSON.stringify(data, null, 2) + '\n', { flag: 'wx' });
  await fs.rename(temporary, p);
}

async function main() {
  const args = parse(process.argv.slice(2));
  if (args.help) {
    console.log('Install complete Skill files offline.\n--skill NAME --agent codex|claude-code|gemini-cli|github-copilot|cursor|generic\n--project PATH | --global | --target SKILL_PARENT_DIRECTORY\n--list --dry-run --verify --upgrade --source PACKAGE_DIRECTORY\nUpdates require --upgrade, a managed unchanged installation, and retain a complete backup.');
    return;
  }
  const sourceRoot = path.resolve(args.source || packageRoot);
  await noSymlinkParents(sourceRoot);
  const names = [];
  for (const entry of await fs.readdir(path.join(sourceRoot, 'skills'), { withFileTypes: true })) {
    if (entry.isDirectory() && await exists(path.join(sourceRoot, 'skills', entry.name, 'SKILL.md'))) names.push(entry.name);
  }
  names.sort();
  if (args.list) { console.log(JSON.stringify({ source: sourceRoot, skills: names, agent_paths: agentPaths }, null, 2)); return; }
  const name = args.skill || (names.length === 1 ? names[0] : '');
  if (!names.includes(name) || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name) || name.length > 64) throw new Error('Choose a valid existing --skill from --list');
  const source = path.join(sourceRoot, 'skills', name);
  await noSymlinkParents(source);
  const front = await fs.readFile(path.join(source, 'SKILL.md'), 'utf8');
  const fm = front.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!fm || !new RegExp(`^name:\\s*["']?${name}["']?\\s*$`, 'm').test(fm[1])) throw new Error('Skill folder and frontmatter name disagree');
  const parent = args.target ? path.resolve(args.target) : path.resolve(args.global ? os.homedir() : args.project, agentPaths[args.agent][args.global ? 1 : 0]);
  const destination = path.join(parent, name);
  if (source === destination || source.startsWith(destination + path.sep) || destination.startsWith(source + path.sep)) throw new Error('Source and destination must not contain each other');
  await noSymlinkParents(parent);
  await noSymlinkParents(destination);
  const desired = await snapshot(source);
  const current = await exists(destination) ? await snapshot(destination) : null;
  if (args.verify) {
    if (!current || !same(current, desired)) throw new Error('Installed files differ from the complete source (including local additions or deletions)');
    console.log(JSON.stringify({ action: 'verified', skill: name, destination, files: Object.keys(desired).length, bytes: Object.values(desired).reduce((n, f) => n + f.size, 0) }));
    return;
  }
  const stateDir = path.join(parent, '.skill-installation');
  const receiptPath = path.join(stateDir, `${name}.json`);
  let prior = null;
  if (await exists(receiptPath)) {
    await noSymlinkParents(receiptPath);
    prior = JSON.parse(await fs.readFile(receiptPath, 'utf8'));
    if (prior.schema !== receiptSchema || prior.skill !== name || prior.destination !== destination || !prior.files) throw new Error('Invalid installation receipt; refusing to overwrite');
  }
  if (current && !same(current, desired)) {
    if (!args.upgrade) throw new Error('Existing different files are preserved; use --upgrade for a clean managed installation');
    if (!prior || !same(current, prior.files)) throw new Error('Local modifications or unmanaged installation are preserved; upgrade refused');
  }
  const action = current ? (same(current, desired) ? 'unchanged' : 'upgraded') : 'installed';
  if (args['dry-run']) { console.log(JSON.stringify({ action, dry_run: true, skill: name, destination, files: Object.keys(desired).length })); return; }
  await fs.mkdir(parent, { recursive: true });
  await fs.mkdir(stateDir, { recursive: true });
  await noSymlinkParents(stateDir);
  const lock = path.join(stateDir, `${name}.lock`);
  try { await fs.mkdir(lock); } catch (e) { if (e.code === 'EEXIST') throw new Error('An installation is already running; no files were changed'); throw e; }
  let stage = null, backup = null;
  try {
    // Recheck after taking the lock so another process cannot overwrite a change silently.
    const latest = await exists(destination) ? await snapshot(destination) : null;
    if ((current === null) !== (latest === null) || (latest && !same(latest, current))) throw new Error('Installation changed concurrently; no files were changed');
    if (action !== 'unchanged') {
      stage = await fs.mkdtemp(path.join(parent, `.${name}-stage-`));
      for (const rel of Object.keys(desired)) {
        const from = path.join(source, rel), to = path.join(stage, rel);
        await fs.mkdir(path.dirname(to), { recursive: true });
        await fs.copyFile(from, to);
        await fs.chmod(to, (await fs.stat(from)).mode & 0o777);
      }
      if (!same(await snapshot(stage), desired)) throw new Error('Staged byte verification failed');
      if (action === 'upgraded') {
        backup = path.join(parent, '.skill-backups', `${name}-${Date.now()}-${randomBytes(4).toString('hex')}`);
        await noSymlinkParents(backup);
        await fs.mkdir(backup, { recursive: true });
        await fs.rename(destination, path.join(backup, 'skill'));
        await fs.copyFile(receiptPath, path.join(backup, 'receipt.json'));
      }
      await fs.rename(stage, destination); stage = null;
    }
    const packageInfo = JSON.parse(await fs.readFile(path.join(sourceRoot, 'package.json'), 'utf8'));
    await atomicJson(receiptPath, { schema: receiptSchema, skill: name, destination, package: packageInfo.name, version: packageInfo.version, installed_at: new Date().toISOString(), files: desired });
    console.log(JSON.stringify({ action, skill: name, destination, files: Object.keys(desired).length, bytes: Object.values(desired).reduce((n, f) => n + f.size, 0), backup }));
  } catch (e) {
    if (backup && !await exists(destination) && await exists(path.join(backup, 'skill'))) await fs.rename(path.join(backup, 'skill'), destination);
    throw e;
  } finally {
    if (stage) await fs.rm(stage, { recursive: true, force: true });
    await fs.rm(lock, { recursive: true, force: true });
  }
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
