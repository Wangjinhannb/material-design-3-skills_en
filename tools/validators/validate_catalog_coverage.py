#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
ROOT=Path(__file__).resolve().parents[2]
sc=yaml.safe_load((ROOT/'metadata/catalog-scenarios.yaml').read_text(encoding='utf-8'))
ids=[x['test_id'] for x in sc['components']]
platforms={
 'web': ['examples/component-catalog/web/index.html'],
 'android': ['examples/component-catalog/android/app/src/main/java/org/example/md3catalog/CatalogScreen.kt'],
 'harmonyos': ['examples/component-catalog/harmonyos/entry/src/main/ets/pages/Index.ets'],
 'ios': ['examples/component-catalog/ios/Sources/CatalogView.swift'],
 'windows': ['examples/component-catalog/windows/MainWindow.xaml'],
 'linux-gtk': ['examples/component-catalog/linux-gtk/main.c'],
 'linux-qt': ['examples/component-catalog/linux-qt/Main.qml'],
}
errors=[]
for platform,files in platforms.items():
    text='\n'.join((ROOT/f).read_text(encoding='utf-8-sig') for f in files)
    missing=[x for x in ids if x not in text]
    if missing: errors.append(f'{platform}: missing {", ".join(missing)}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'Catalog coverage passed: {len(ids)} components x {len(platforms)} platforms')
