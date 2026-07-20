PYTHON ?= python3

.PHONY: all check validate test package verify-dist sync-manifest clean-dist site-install site-dev site-build site-check help

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

## site-install: Install locked Fieldbook dependencies
site-install:
	npm --prefix site ci

## site-dev: Start the local Fieldbook development server
site-dev:
	npm --prefix site run dev

## site-build: Build the static GitHub Pages Fieldbook
site-build:
	npm --prefix site run build

## site-check: Test, build, and verify the Fieldbook
site-check:
	npm --prefix site run check

## help: Show available targets
help:
	@grep -E '^##' Makefile | sed -e 's/## //'
