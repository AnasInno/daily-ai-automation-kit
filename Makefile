.PHONY: check doctor smoke test safety clean

check: doctor smoke test safety

doctor:
	python3 scripts/repo_doctor.py

smoke:
	python3 scripts/verify_examples.py --smoke

test:
	python3 scripts/verify_examples.py --test

safety:
	python3 scripts/public_safety_check.py .

clean:
	rm -rf .pytest_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
