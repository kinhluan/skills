PYTHON ?= python3

.PHONY: all check validate test package verify-dist sync-manifest clean-dist help

all: check

## check: Validate sources, run tests, and verify committed packages
check: validate test verify-dist

## validate: Validate skill sources, metadata, links, routing, and release config
validate:
	$(PYTHON) scripts/validate_skills.py

## test: Run the repository test suite
test:
	$(PYTHON) -m unittest discover -s tests -v

## sync-manifest: Rebuild skills.json entries from canonical skill sources
sync-manifest:
	$(PYTHON) scripts/sync_manifest.py

## package: Validate, test, and rebuild deterministic .skill packages
package: validate test
	$(PYTHON) scripts/package_skills.py

## verify-dist: Check that dist exactly matches canonical skill sources
verify-dist:
	$(PYTHON) scripts/package_skills.py --check

## clean-dist: Remove generated .skill packages only
clean-dist:
	$(PYTHON) scripts/package_skills.py --clean

## help: Show available targets
help:
	@grep -E '^##' Makefile | sed -e 's/## //'
