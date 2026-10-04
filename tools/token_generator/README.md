# Token Generator

Run:

```bash
python tools/token_generator/generate.py
```

The generator reads canonical files under `tokens/source/` and writes platform mappings under `tokens/generated/`.

Generated output is checked for determinism. Edit token source files rather than generated platform files.
