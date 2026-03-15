# Makefile for AI Agent Skills

# Paths
SKILL_CREATOR_DIR = /Users/luan.bui/.agents/skills/skill-creator/scripts
SOURCE_DIR = .agent-skills
DIST_DIR = dist

# Scripts
PACKAGE_SCRIPT = python3 $(SKILL_CREATOR_DIR)/package_skill.py
VALIDATE_SCRIPT = python3 $(SKILL_CREATOR_DIR)/quick_validate.py

# Find all skill directories (excluding hidden ones)
SKILLS = $(shell find $(SOURCE_DIR) -maxdepth 1 -mindepth 1 -type d)

.PHONY: all package validate clean help

all: package

## package: Pack all skills into .skill files in dist/
package: clean-dist
	@mkdir -p $(DIST_DIR)
	@echo "📦 Packaging all skills..."
	@$(foreach skill,$(SKILLS), $(PACKAGE_SCRIPT) $(skill) $(DIST_DIR);)
	@echo "✅ All skills packaged successfully in $(DIST_DIR)/"

## validate: Run validation check on all skills
validate:
	@echo "🔍 Validating all skills..."
	@$(foreach skill,$(SKILLS), $(PACKAGE_SCRIPT) $(skill) --validate-only;)
	@echo "✅ Validation complete."

## clean-dist: Remove all packaged skills from dist/
clean-dist:
	@echo "🧹 Cleaning $(DIST_DIR)..."
	@rm -rf $(DIST_DIR)/*.skill

## help: Show this help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^##' Makefile | sed -e 's/## //'
