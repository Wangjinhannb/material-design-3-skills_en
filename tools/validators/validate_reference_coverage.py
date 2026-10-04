#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = yaml.safe_load((ROOT / 'examples/reference-app/reference-spec.yaml').read_text(encoding='utf-8-sig'))
markers = [f"reference-{name}" for name in spec['sections']]
sources = {
    'web': ROOT / 'examples/reference-app/web/index.html',
    'android': ROOT / 'examples/reference-app/android/app/src/main/java/org/example/md3reference/MainActivity.kt',
    'harmonyos': ROOT / 'examples/reference-app/harmonyos/entry/src/main/ets/pages/Index.ets',
    'ios': ROOT / 'examples/reference-app/ios/Sources/ContentView.swift',
    'windows': ROOT / 'examples/reference-app/windows/MainWindow.xaml',
    'linux-gtk': ROOT / 'examples/reference-app/linux-gtk/main.c',
    'linux-qt': ROOT / 'examples/reference-app/linux-qt/Main.qml',
}
errors = []
for platform, path in sources.items():
    if not path.exists():
        errors.append(f'{platform}: missing {path.relative_to(ROOT)}')
        continue
    text = path.read_text(encoding='utf-8-sig')
    missing = [m for m in markers if m not in text]
    if missing:
        errors.append(f"{platform}: missing {', '.join(missing)}")
if errors:
    raise SystemExit('\n'.join(errors))
print(f"Reference coverage passed: {len(markers)} sections x {len(sources)} platforms")
