.PHONY: smoke test clean

smoke:
	python3 scripts/run.py --input data/sample_teachclaw_request.json --output output/sample_proof_packet.md

test:
	python3 -m pytest -q

clean:
	rm -f output/sample_proof_packet.md
