# Validation Report

Core repository validation:

```bash
python tools/token_generator/generate.py
python tools/component_generator/generate_component_docs.py
python tools/support_matrix/generate.py
python tools/source_checker/check_sources.py
python tools/validators/validate_repo.py
python tools/validators/check_writing_style.py
python tools/validators/check_english_only.py
python tools/validators/validate_catalog_coverage.py
python tools/validators/validate_reference_coverage.py
python tools/validators/validate_skill_evals.py
python tools/validators/check_generated_determinism.py
python -m unittest discover -s tests -p 'test_*.py'
```

Platform builds are recorded by GitHub Actions. HarmonyOS runtime verification remains a DevEco Studio/self-hosted-runner task.
