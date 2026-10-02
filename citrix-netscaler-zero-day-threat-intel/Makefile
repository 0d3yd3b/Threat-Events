.PHONY: validate summary serve

validate:
	python3 scripts/validate_iocs.py

summary:
	python3 scripts/build_ioc_summary.py

serve:
	python3 -m http.server 8000 --directory .
