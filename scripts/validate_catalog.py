#!/usr/bin/env python3
"""Offline structural checks only. Does not execute mods or check live URLs."""
import datetime
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
payload = json.loads((ROOT / 'data/mods.json').read_text())
entries = payload['entries']
assert entries, 'No entries'
ids = set()
urls = set()
for entry in entries:
    for key in ('id', 'name', 'author', 'url', 'kind', 'summary', 'summary_zh', 'caveats', 'license_note', 'upstream_version_evidence', 'review', 'evidence'):
        assert entry.get(key), f"{entry.get('id')}: missing {key}"
    assert entry['id'] not in ids, f"Duplicate id: {entry['id']}"
    assert entry['url'] not in urls, f"Duplicate mod URL: {entry['url']}"
    ids.add(entry['id']); urls.add(entry['url'])
    parsed = urlparse(entry['url'])
    assert parsed.scheme == 'https' and parsed.netloc == 'github.com'
    assert entry['author'] == entry['repository'].split('/')[0]
    datetime.date.fromisoformat(entry['review']['checked_on'])
    level = entry['review']['level']
    assert level in {'documentation-and-entry-checked', 'static-validated', 'runtime-tested', 'blocked'}
    if level == 'runtime-tested':
        assert entry['review'].get('tests_run'), 'Runtime-tested claims require evidence'
    ev = entry['evidence']
    for key in ('readme', 'entry', 'module'):
        assert ev.get(key) and re.fullmatch(r'[0-9a-f]{40}', ev[key]['sha']), f"{entry['id']}: incomplete {key} identity"
    assert ev['entry']['url'].endswith('/hooks/hooks.json'), f"{entry['id']}: entry should identify hooks declaration"
    assert ev['entry']['modules'], f"{entry['id']}: no declared modules"
    for name in ('README.md','README.zh-CN.md'):
        assert entry['url'] in (ROOT / name).read_text(), f"{entry['id']}: missing from {name}"
# Relative Markdown links must point to files within this repository.
relative_count=0
for source in ROOT.rglob('*.md'):
    for target in re.findall(r'\]\(([^)\s]+)\)', source.read_text()):
        if '://' in target or target.startswith('#') or target.startswith('mailto:'): continue
        path = (source.parent / target.split('#',1)[0]).resolve()
        assert path.is_relative_to(ROOT), f'Link escapes repository: {source}: {target}'
        assert path.exists(), f'Broken local link: {source}: {target}'
        relative_count+=1
print(f'PASS: {len(entries)} unique entries, source identities, bilingual coverage, {relative_count} relative links')
print('Live availability, Claude compatibility, security, and mod execution were NOT tested.')
