#!/usr/bin/env python3
"""
Validate all skills against skills.sh standard.
Checks: YAML frontmatter, required fields, file existence, SKILL.toon presence.
"""
import os
import sys
import yaml
import json
from pathlib import Path

SKILLS_DIR = Path('.agent-skills')
REQUIRED_FIELDS = ['name', 'description']
RECOMMENDED_FIELDS = ['metadata.tags']
MAX_DESCRIPTION_LENGTH = 200

def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    warnings = []
    
    skill_md = skill_dir / 'SKILL.md'
    skill_toon = skill_dir / 'SKILL.toon'
    
    # Check SKILL.md exists
    if not skill_md.exists():
        errors.append(f"{skill_dir.name}: SKILL.md not found")
        return errors
    
    # Check SKILL.toon exists
    if not skill_toon.exists():
        warnings.append(f"{skill_dir.name}: SKILL.toon not found (recommended)")
    
    # Parse YAML frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        errors.append(f"{skill_dir.name}: Missing YAML frontmatter")
        return errors
    
    try:
        parts = content.split('---', 2)
        if len(parts) < 3:
            errors.append(f"{skill_dir.name}: Invalid frontmatter format")
            return errors
        
        frontmatter = yaml.safe_load(parts[1])
        if not frontmatter:
            errors.append(f"{skill_dir.name}: Empty frontmatter")
            return errors
        
        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in frontmatter:
                errors.append(f"{skill_dir.name}: Missing required field '{field}'")
        
        # Check description length
        desc = frontmatter.get('description', '')
        if len(desc) > MAX_DESCRIPTION_LENGTH:
            warnings.append(f"{skill_dir.name}: Description too long ({len(desc)} chars, max {MAX_DESCRIPTION_LENGTH})")
        
        # Check metadata.tags
        metadata = frontmatter.get('metadata') or {}
        if 'tags' not in metadata:
            warnings.append(f"{skill_dir.name}: Missing metadata.tags")
        
        # Check name matches directory
        if frontmatter.get('name') != skill_dir.name:
            errors.append(f"{skill_dir.name}: Name in frontmatter doesn't match directory")
        
    except yaml.YAMLError as e:
        errors.append(f"{skill_dir.name}: YAML parse error: {e}")
    
    return errors + warnings

def validate_skills_json() -> list[str]:
    errors = []
    
    skills_json = Path('skills.json')
    if not skills_json.exists():
        errors.append("skills.json not found")
        return errors
    
    try:
        with open(skills_json) as f:
            data = json.load(f)
        
        if 'skills' not in data:
            errors.append("skills.json missing 'skills' array")
            return errors
        
        # Check each skill entry
        skill_names = set()
        for skill in data['skills']:
            name = skill.get('name')
            if not name:
                errors.append("skills.json: skill entry missing 'name'")
                continue
            
            if name in skill_names:
                errors.append(f"skills.json: duplicate skill name '{name}'")
            skill_names.add(name)
            
            if 'path' not in skill:
                errors.append(f"skills.json: '{name}' missing 'path'")
            elif not Path(skill['path']).exists():
                errors.append(f"skills.json: '{name}' path '{skill['path']}' doesn't exist")
        
        # Check for skills in directory but not in json
        for skill_dir in SKILLS_DIR.iterdir():
            if skill_dir.is_dir() and skill_dir.name not in skill_names:
                errors.append(f"skills.json: '{skill_dir.name}' exists in directory but not in json")
        
    except json.JSONDecodeError as e:
        errors.append(f"skills.json: JSON parse error: {e}")
    
    return errors

def main():
    errors = []
    warnings = []
    
    # Validate skills.json
    json_errors = validate_skills_json()
    errors.extend(json_errors)
    
    # Validate each skill
    if SKILLS_DIR.exists():
        for skill_dir in sorted(SKILLS_DIR.iterdir()):
            if skill_dir.is_dir():
                result = validate_skill(skill_dir)
                for item in result:
                    if 'not found' in item or 'Missing' in item or 'Invalid' in item or 'doesn' in item:
                        errors.append(item)
                    else:
                        warnings.append(item)
    
    # Report
    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    
    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"✅ All skills valid! ({len(list(SKILLS_DIR.iterdir()))} skills)")
        sys.exit(0)

if __name__ == '__main__':
    main()
