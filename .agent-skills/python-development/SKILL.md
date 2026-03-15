---
name: python-development
description: Python programming best practices, patterns, and tips
metadata:
---

# Python Development

Best practices and patterns for Python development.

## When to Use

- Writing Python scripts or applications
- Code review and refactoring
- Setting up new Python projects

## Guidelines

### Code Style

- Follow PEP 8 style guide
- Use type hints for function signatures
- Write docstrings for public functions and classes

### Project Structure

```
project/
├── src/
│   └── package/
├── tests/
├── pyproject.toml
└── README.md
```

### Common Patterns

#### Context Managers

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire()
    try:
        yield resource
    finally:
        release(resource)
```

#### Data Classes

```python
from dataclasses import dataclass

@dataclass
class Config:
    host: str
    port: int
    debug: bool = False
```

## Resources

- [Python Official Docs](https://docs.python.org/)
- [PEP 8 Style Guide](https://pep8.org/)
