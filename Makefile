test:
	cd phase2 && python -m pytest tests -q

verify:
	cd phase2/results/v2 && sha256sum -c SHA256SUMS.txt
