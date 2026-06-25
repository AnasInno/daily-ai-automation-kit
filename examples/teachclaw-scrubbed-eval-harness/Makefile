.PHONY: smoke test clean

smoke:
	python3 scripts/run_eval.py --scenarios data/scenarios.json --rubric data/rubric.json --runs data/candidate_runs.json --output-dir output

test:
	python3 -m pytest -q

clean:
	rm -f output/eval_scorecard.json output/eval_scorecard.md
