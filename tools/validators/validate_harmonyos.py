#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
projects=[ROOT/'examples/component-catalog/harmonyos',ROOT/'examples/reference-app/harmonyos']
required=['AppScope/app.json5','build-profile.json5','hvigorfile.ts','oh-package.json5','entry/build-profile.json5','entry/hvigorfile.ts','entry/oh-package.json5','entry/src/main/module.json5','entry/src/main/resources/base/profile/main_pages.json','entry/src/main/ets/pages/Index.ets']
errors=[]
for project in projects:
    for rel in required:
        if not (project/rel).is_file(): errors.append(f'{project.name}: missing {rel}')
    page=(project/'entry/src/main/ets/pages/Index.ets')
    if page.is_file():
        text=page.read_text(encoding='utf-8')
        if '@Entry' not in text or '@Component' not in text or 'build()' not in text: errors.append(f'{project.name}: invalid ArkUI page entry')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('HarmonyOS static validation passed')
