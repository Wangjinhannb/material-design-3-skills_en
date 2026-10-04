.PHONY: generate validate test check package-skill

generate:
	python tools/token_generator/generate.py
	python tools/component_generator/generate_component_docs.py
	python tools/support_matrix/generate.py

validate:
	python tools/validators/validate_repo.py
	python tools/validators/check_writing_style.py
	python tools/validators/check_english_only.py
	python tools/validators/validate_catalog_coverage.py
	python tools/validators/validate_reference_coverage.py
	python tools/validators/validate_harmonyos.py
	python tools/validators/validate_skill_evals.py
	python tools/validators/check_generated_determinism.py

test:
	python -m unittest discover -s tests -p 'test_*.py'
	node --check examples/reference-app/web/app.js
	node --check examples/component-catalog/web/app.js
	node --check examples/component-catalog/web/playwright.config.js

check: generate validate test

package-skill:
	python tools/skill_packager/package.py
