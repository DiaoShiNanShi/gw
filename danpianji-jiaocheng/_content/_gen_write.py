#!/usr/bin/env python3
"""Write mod_*.py, nav.py, __init__.py from generated ALL list."""
from pathlib import Path
import re
import _gen_part3  # noqa: F401 — builds ALL (80 chapters)
from _gen_part1 import ALL

OUT = Path(__file__).parent

MODULES = {
    'mod_base.py': [c for c in ALL if c[0].startswith('基础/')],
    'mod_hardware.py': [c for c in ALL if c[0].startswith('硬件/')],
    'mod_protocol.py': [c for c in ALL if c[0].startswith('协议/')],
    'mod_practice.py': [c for c in ALL if c[0].startswith('入门实战/')],
    'mod_stm32.py': [c for c in ALL if c[0].startswith('STM32/')],
    'mod_esp32.py': [c for c in ALL if c[0].startswith('ESP32/')],
    'mod_advanced.py': [c for c in ALL if c[0].startswith('进阶/')],
    'mod_ios.py': [c for c in ALL if c[0].startswith('iOS联动/')],
    'mod_projects.py': [c for c in ALL if c[0].startswith('项目实战/')],
    'mod_scenarios.py': [c for c in ALL if c[0].startswith('应用场景/')],
    'mod_exercises.py': [c for c in ALL if c[0].startswith('练习/')],
    'mod_interview.py': [c for c in ALL if c[0].startswith('面试题/')],
}

total = sum(len(v) for v in MODULES.values())
assert total == 80, f'Expected 80 chapters, got {total}'
assert len(ALL) == 80, f'ALL len {len(ALL)}'


def validate(path, body):
    assert len(body) >= 1500, f'{path}: body len {len(body)}'
    assert '<table' in body, f'{path}: missing table'
    assert '<pre><code' in body, f'{path}: missing code'
    assert 'tip-box' in body, f'{path}: missing tip'
    assert '常见问题' in body, f'{path}: missing faq'
    assert '本章小结' in body, f'{path}: missing summary'


for path, meta in ALL:
    validate(path, meta['body'])


def write_module(fname, chapters):
    lines = [
        '"""Chapter content definitions."""',
        '',
        'from .helpers import chapter',
        '',
        'CHAPTERS = {',
    ]
    for path, meta in chapters:
        body = meta['body'].replace('\\', '\\\\')
        if '"""' in body:
            body = body.replace('"""', '\\"\\"\\"')
        lines.append(f'    "{path}": chapter(')
        lines.append(f'        {meta["title"]!r},')
        lines.append(f'        {meta["tag"]!r},')
        lines.append(f'        {meta["module"]!r},')
        lines.append(f'        """{body}""",')
        lines.append('    ),')
    lines.append('}')
    (OUT / fname).write_text('\n'.join(lines) + '\n', encoding='utf-8')


for fname, chs in MODULES.items():
    write_module(fname, chs)

# nav.py
NAV_META = [
    ('home', '教程首页', None, 'README.html'),
    ('base', '基础', 'mod_base'),
    ('hw', '硬件入门', 'mod_hardware'),
    ('proto', '协议', 'mod_protocol'),
    ('start', '入门实战', 'mod_practice'),
    ('stm32', 'STM32', 'mod_stm32'),
    ('esp32', 'ESP32', 'mod_esp32'),
    ('adv', '进阶', 'mod_advanced'),
    ('ios', 'iOS 联动', 'mod_ios'),
    ('proj', '项目实战', 'mod_projects'),
    ('scene', '应用场景', 'mod_scenarios'),
    ('exercise', '练习', 'mod_exercises'),
    ('interview', '面试题', 'mod_interview'),
]

nav_lines = ['"""Site navigation matching _build_site.py format."""', '', 'NAV = [']
nav_lines.append('    {"id": "home", "title": "教程首页", "href": "README.html"},')

for sid, stitle, mod_key, *rest in NAV_META[1:]:
    chs = MODULES[mod_key + '.py']
    nav_lines.append(f'    {{"id": "{sid}", "title": "{stitle}", "items": [')
    for path, meta in chs:
        num = path.split('/')[-1].split('-')[0]
        slug = path.split('/')[-1].replace('.html', '')
        if '-' in slug:
            slug = slug.split('-', 1)[1]
        label = meta['title'].split('：')[-1] if '：' in meta['title'] else meta['title']
        short = f'{num} {label[:16]}'
        nav_lines.append(f'        ({short!r}, {path!r}),')
    nav_lines.append('    ]},')

nav_lines.append(']')
(OUT / 'nav.py').write_text('\n'.join(nav_lines) + '\n', encoding='utf-8')

init = '''"""Merged chapters and navigation."""
from .mod_base import CHAPTERS as _BASE
from .mod_hardware import CHAPTERS as _HW
from .mod_protocol import CHAPTERS as _PROTO
from .mod_practice import CHAPTERS as _PRACTICE
from .mod_stm32 import CHAPTERS as _STM32
from .mod_esp32 import CHAPTERS as _ESP32
from .mod_advanced import CHAPTERS as _ADV
from .mod_ios import CHAPTERS as _IOS
from .mod_projects import CHAPTERS as _PROJ
from .mod_scenarios import CHAPTERS as _SCENE
from .mod_exercises import CHAPTERS as _EX
from .mod_interview import CHAPTERS as _INT
from .nav import NAV

CHAPTERS = {}
for _m in (_BASE, _HW, _PROTO, _PRACTICE, _STM32, _ESP32, _ADV, _IOS, _PROJ, _SCENE, _EX, _INT):
    CHAPTERS.update(_m)

TOTAL = len(CHAPTERS)

__all__ = ["NAV", "CHAPTERS", "TOTAL"]
'''
(OUT / '__init__.py').write_text(init, encoding='utf-8')

print(f'Generated {total} chapters in {len(MODULES)} module files + nav.py + __init__.py')
for k, v in MODULES.items():
    print(f'  {k}: {len(v)}')
