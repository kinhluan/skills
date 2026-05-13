---
name: python-development
description: Modern Python development best practices (2024-2025). Use this skill for project setup, dependency management, typing, testing, linting, async patterns, FastAPI, SQLAlchemy, Pydantic, and production deployment.
metadata:
  tags: ["python", "programming", "backend", "typing", "testing", "async", "fastapi", "pydantic", "sqlalchemy", "packaging", "linting", "ruff"]
---

# Python Development

Modern Python development covering project configuration, typing, testing, linting, async, web frameworks, ORM, and production patterns. Targets Python 3.10+ with focus on 3.12+ features.

> "There should be one — and preferably only one — obvious way to do it." — The Zen of Python

---

## 1. Project Configuration (`pyproject.toml`)

Single source of truth for project metadata, dependencies, and tool config.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-app"
version = "0.1.0"
description = "My application"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115",
    "uvicorn[standard]>=0.30",
    "sqlalchemy[asyncio]>=2.0",
    "pydantic>=2.0",
    "pydantic-settings>=2.0",
    "structlog>=24.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-cov>=5.0",
    "pytest-asyncio>=0.24",
    "ruff>=0.5",
    "mypy>=1.10",
    "pre-commit>=3.7",
]
docs = ["mkdocs-material>=9.0"]

[project.scripts]
my-app = "my_app.cli:main"

[tool.hatch.build.targets.wheel]
packages = ["src/my_app"]
```

**Build backends:** `hatchling` (default, modern), `setuptools` (legacy), `flit-core` (simple), `maturin` (Rust extensions).

**Src layout** (recommended):
```
project/
├── src/
│   └── my_app/
│       ├── __init__.py
│       ├── __main__.py
│       ├── api/
│       ├── core/
│       ├── models/
│       └── services/
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── pyproject.toml
└── README.md
```

---

## 2. Dependency Management

### uv (Recommended, 2024+)

```bash
uv venv                          # create venv
uv pip install -e ".[dev]"       # install with dev deps
uv pip compile pyproject.toml -o requirements.txt  # lock
uv sync                          # install from lock
```

### Poetry

```bash
poetry init
poetry add fastapi sqlalchemy
poetry add --group dev pytest ruff mypy
poetry install
poetry build
```

### pip-tools

```bash
pip-compile pyproject.toml -o requirements.txt
pip install -r requirements.txt
```

### Virtual Environments

```bash
python -m venv .venv             # stdlib
source .venv/bin/activate        # activate
uv venv --python 3.12            # uv with specific version
```

**`.python-version`** file for pyenv/asdf:
```
3.12.4
```

---

## 3. Modern Typing

### Type Aliases & Syntax (PEP 604, 613, 695)

```python
# Union syntax (3.10+)
def process(value: int | str | None) -> str: ...

# Type alias (3.12+)
type Vector = list[float]
type UserId = int

# TypeAlias (3.10+)
from typing import TypeAlias
Vector: TypeAlias = list[float]
```

### Generics (3.12+)

```python
# Modern syntax
def first[T](items: list[T]) -> T:
    return items[0]

class Repository[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None: ...
    def get(self, id: int) -> T | None: ...
```

### Protocol (Structural Typing)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Renderable(Protocol):
    def render(self) -> str: ...

class Report:
    def render(self) -> str:
        return "report data"

# Report satisfies Renderable without inheritance
def print_item(item: Renderable) -> None:
    print(item.render())
```

### Self, TypeGuard, Annotated

```python
from typing import Self, TypeGuard, Annotated

class Builder:
    def with_name(self, name: str) -> Self:
        self.name = name
        return self

def is_string_list(val: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

# Annotated for metadata
PositiveInt = Annotated[int, Field(gt=0)]
```

### TypedDict & Literal

```python
from typing import TypedDict, Literal

class ApiResponse(TypedDict):
    status: Literal["ok", "error"]
    data: dict[str, Any]
    message: str
```

### When to Use What

| Type construct | Use case |
|---|---|
| `Protocol` | Interface without inheritance (ports/adapters) |
| `ABC` | Shared implementation + enforced contract |
| `TypeVar` / generics | Type-safe containers, functions |
| `TypedDict` | Typed dictionaries (JSON-like data) |
| `Literal` | Constrain to specific values |
| `Enum` | Named constants with behavior |
| `dataclass` | Simple data containers |
| `Pydantic BaseModel` | Validation + serialization at boundaries |

---

## 4. Linting, Formatting & Static Analysis

### Ruff (2024+ standard)

Replaces flake8, black, isort, pyupgrade, and more.

```toml
# pyproject.toml
[tool.ruff]
target-version = "py312"
line-length = 88

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "F",    # pyflakes
    "W",    # pycodestyle warnings
    "I",    # isort
    "N",    # pep8-naming
    "UP",   # pyupgrade
    "B",    # flake8-bugbear
    "A",    # flake8-builtins
    "SIM",  # flake8-simplify
    "PT",   # flake8-pytest-style
    "RUF",  # ruff-specific
    "S",    # flake8-bandit (security)
    "LOG",  # flake8-logging
]
ignore = ["E501"]  # line length handled by formatter

[tool.ruff.lint.isort]
known-first-party = ["my_app"]

[tool.ruff.format]
quote-style = "double"
```

```bash
ruff check .           # lint
ruff check . --fix     # auto-fix
ruff format .          # format (replaces black)
```

### mypy (Static Type Checking)

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

# Per-module overrides
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

```bash
mypy src/
```

### Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.5.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
        additional_dependencies: [pydantic, types-requests]
```

---

## 5. Pydantic v2

Validation + serialization at system boundaries (API, config, DB).

```python
from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic import ConfigDict
from decimal import Decimal

class OrderItem(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, frozen=True)

    product_id: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    unit_price: Decimal = Field(..., ge=0)

    @field_validator("product_id")
    @classmethod
    def validate_product_id(cls, v: str) -> str:
        if not v.startswith("PROD-"):
            raise ValueError("Product ID must start with PROD-")
        return v

class Order(BaseModel):
    customer_id: str
    items: list[OrderItem]

    @model_validator(mode="after")
    def validate_min_items(self) -> "Order":
        if len(self.items) == 0:
            raise ValueError("Order must have at least one item")
        return self

    @property
    def total(self) -> Decimal:
        return sum(item.unit_price * item.quantity for item in self.items)
```

### Settings Management

```python
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

    debug: bool = False
    database_url: str = Field(..., description="PostgreSQL connection string")
    api_key: str = Field(..., min_length=10)
    log_level: str = "INFO"

settings = Settings()  # reads from env vars / .env
```

### Serialization

```python
order = Order(customer_id="C1", items=[...])

order.model_dump()                    # → dict
order.model_dump(mode="json")         # JSON-safe (Decimal → str)
order.model_dump(exclude_unset=True)  # only explicitly set fields
order.model_dump_json()               # → JSON string
Order.model_validate_json(json_str)   # parse JSON
```

---

## 6. Async / Await

### Core Patterns

```python
import asyncio

async def fetch_user(user_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status()
        return response.json()

# Concurrent execution
async def fetch_all(user_ids: list[int]) -> list[dict]:
    tasks = [fetch_user(uid) for uid in user_ids]
    return await asyncio.gather(*tasks)

# Structured concurrency (3.11+)
async def fetch_all_v2(user_ids: list[int]) -> list[dict]:
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch_user(uid)) for uid in user_ids]
    return [t.result() for t in tasks]
```

### Semaphore for Rate Limiting

```python
sem = asyncio.Semaphore(10)

async def limited_fetch(url: str) -> str:
    async with sem:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            return resp.text
```

### Async Context Manager

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_db_session():
    async with AsyncSession(engine) as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```

### Common Pitfalls

| Pitfall | Fix |
|---|---|
| `time.sleep()` in async code | Use `await asyncio.sleep()` |
| `requests.get()` in async code | Use `httpx.AsyncClient` |
| Blocking I/O in async | `await asyncio.to_thread(blocking_fn)` |
| Forgetting `await` | mypy/ruff will catch; always `await` coroutines |

---

## 7. Testing

### pytest Core

```python
# tests/test_order.py
import pytest
from my_app.models import Order, OrderItem

class TestOrder:
    def test_total_calculation(self):
        order = Order(
            customer_id="C1",
            items=[
                OrderItem(product_id="PROD-1", quantity=2, unit_price=Decimal("10.00")),
                OrderItem(product_id="PROD-2", quantity=1, unit_price=Decimal("25.00")),
            ],
        )
        assert order.total == Decimal("45.00")

    def test_empty_order_raises(self):
        with pytest.raises(ValueError, match="at least one item"):
            Order(customer_id="C1", items=[])
```

### Fixtures

```python
# tests/conftest.py
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

@pytest.fixture
def sample_order() -> Order:
    return Order(
        customer_id="C1",
        items=[OrderItem(product_id="PROD-1", quantity=1, unit_price=Decimal("10"))],
    )

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def db_session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSession(engine) as session:
        yield session
```

### Parametrize

```python
@pytest.mark.parametrize(
    "quantity, price, expected",
    [
        (1, Decimal("10"), Decimal("10")),
        (0, Decimal("10"), Decimal("0")),
        (5, Decimal("3.50"), Decimal("17.50")),
    ],
)
def test_subtotal(quantity, price, expected):
    item = OrderItem(product_id="PROD-1", quantity=quantity, unit_price=price)
    assert item.subtotal == expected
```

### Mocking

```python
from unittest.mock import AsyncMock, patch

@pytest.fixture
def mock_email_service():
    return AsyncMock()

async test_send_notification(mock_email_service):
    service = NotificationService(email=mock_email_service)
    await service.notify_user("user-1", "Hello")
    mock_email_service.send.assert_awaited_once_with("user-1", "Hello")

# Patching
@patch("my_app.services.requests.get")
def test_external_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": "ok"}
    result = call_external_api()
    assert result == {"result": "ok"}
```

### pytest Config

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
addopts = "-ra -q --strict-markers --strict-config"
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: integration tests requiring external services",
]

[tool.coverage.run]
source = ["src/my_app"]
branch = true

[tool.coverage.report]
show_missing = true
fail_under = 80
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "if __name__ == .__main__.",
]
```

---

## 8. FastAPI Patterns

### Application Structure

```python
# src/my_app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await init_db()
    yield
    # shutdown
    await close_db()

app = FastAPI(title="My App", lifespan=lifespan)
```

### Router with Dependency Injection

```python
# src/my_app/api/orders.py
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/orders", tags=["orders"])

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = await verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

@router.post("/", response_model=OrderResponse, status_code=201)
async def create_order(
    body: OrderCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    order = OrderService(db)
    return await order.create(user_id=user.id, items=body.items)

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: str,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    order = await db.get(Order, order_id)
    if not order or (order.user_id != user.id and not user.is_admin):
        raise HTTPException(status_code=404, detail="Order not found")
    return order
```

### Error Handling

```python
from fastapi import Request
from fastapi.responses import JSONResponse

class AppError(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_error_handler(request: Request, exc: Exception):
    logger.error("Unhandled error", exc_info=True, path=request.url.path)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"},
    )
```

---

## 9. SQLAlchemy 2.0

### Declarative Models

```python
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from uuid import UUID, uuid4

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    customer_id: Mapped[UUID] = mapped_column(ForeignKey("customers.id"))
    status: Mapped[str] = mapped_column(String(20), default="PENDING")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    items: Mapped[list["OrderItem"]] = relationship(back_populates="order", cascade="all, delete-orphan")
    customer: Mapped["Customer"] = relationship(back_populates="orders")

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"))
    product_id: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int] = mapped_column()
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    order: Mapped["Order"] = relationship(back_populates="items")
```

### Async Session

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db", echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

# Usage in service
async def create_order(db: AsyncSession, customer_id: UUID, items: list[dict]) -> Order:
    order = Order(customer_id=customer_id)
    for item_data in items:
        order.items.append(OrderItem(**item_data))
    db.add(order)
    await db.commit()
    return order
```

### Alembic Migrations

```bash
alembic init migrations
alembic revision --autogenerate -m "add orders table"
alembic upgrade head
alembic downgrade -1
```

```ini
# alembic.ini
[alembic]
script_location = migrations
sqlalchemy.url = postgresql+asyncpg://user:pass@localhost/db
```

---

## 10. Error Handling & Logging

### Custom Exception Hierarchy

```python
class AppError(Exception):
    """Base error for application."""
    def __init__(self, message: str, code: str = "APP_ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)

class NotFoundError(AppError):
    def __init__(self, resource: str, id: str):
        super().__init__(f"{resource} {id} not found", "NOT_FOUND")

class ValidationError(AppError):
    def __init__(self, detail: str):
        super().__init__(detail, "VALIDATION_ERROR")

class ConflictError(AppError):
    def __init__(self, detail: str):
        super().__init__(detail, "CONFLICT")
```

### Exception Chaining

```python
try:
    result = await external_api.fetch(data)
except httpx.HTTPStatusError as e:
    raise AppError("External service unavailable") from e
```

### Structured Logging

```python
import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer() if settings.debug else structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(
        logging.getLevelName(settings.log_level)
    ),
)

logger = structlog.get_logger()

# Usage
logger.info("order_created", order_id=str(order.id), total=str(order.total))
logger.error("payment_failed", order_id=str(order.id), reason=str(exc))
```

### Request Context

```python
import structlog
from contextvars import ContextVar

request_id_ctx: ContextVar[str] = ContextVar("request_id", default="")

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid4()))
    request_id_ctx.set(request_id)
    structlog.contextvars.bind_contextvars(request_id=request_id)
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response
```

---

## 11. Performance & Optimization

### Profiling

```bash
# cProfile
python -m cProfile -s cumulative my_script.py

# py-spy (sampling, no code changes)
py-spy top --pid 12345
py-spy record -o profile.svg -- python my_script.py

# memray (memory)
memray run my_script.py
memray flamegraph output.bin
```

### Caching

```python
from functools import lru_cache, cache

@lru_cache(maxsize=256)
def expensive_computation(n: int) -> int: ...

@cache  # unbounded (3.9+)
def get_config() -> dict: ...
```

### Concurrency

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio

# CPU-bound → ProcessPoolExecutor
def cpu_task(data):
    return heavy_computation(data)

async def run_cpu_tasks(data_list):
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, cpu_task, d) for d in data_list]
    return await asyncio.gather(*tasks)

# I/O-bound → asyncio (preferred) or ThreadPoolExecutor
```

### Memory Optimization

```python
# __slots__ for high-volume objects
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Slots dataclass (3.10+)
@dataclass(slots=True)
class Point:
    x: float
    y: float

# Generators for large datasets
def read_large_file(path: str):
    with open(path) as f:
        for line in f:
            yield process(line)
```

---

## 12. Docker for Python

```dockerfile
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

FROM base AS deps
COPY pyproject.toml .
RUN pip install --no-cache-dir .

FROM deps AS runtime
COPY src/ src/
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "my_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**`.dockerignore`:**
```
__pycache__
*.pyc
.venv
.mypy_cache
.ruff_cache
.pytest_cache
.git
tests/
docs/
```

**Production:** Use gunicorn with uvicorn workers:
```bash
gunicorn my_app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

---

## 13. CLI Tools

### Typer (Recommended)

```python
import typer
from typing import Optional

app = typer.Typer(help="My CLI tool")

@app.command()
def greet(name: str, uppercase: bool = False):
    """Greet someone."""
    msg = f"Hello, {name}!"
    if uppercase:
        msg = msg.upper()
    typer.echo(msg)

@app.command()
def process(
    input_file: typer.FileText,
    output: Optional[typer.FileTextWrite] = None,
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    """Process input file."""
    data = input_file.read()
    result = transform(data)
    if output:
        output.write(result)
    else:
        typer.echo(result)

if __name__ == "__main__":
    app()
```

---

## 14. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| FastAPI basics | `security-analysis` | OWASP patterns, auth, rate limiting |
| dataclass patterns | `ddd-tactical` | Domain modeling, Value Objects, Entities |
| Protocol typing | `c4-level4-code` | Hexagonal architecture, ports/adapters |
| pytest patterns | `evolutionary-architecture` | Fitness functions, architecture tests |
| Project structure | `c4-level3-component` | Folder mapping, dependency boundaries |
| Ruff adoption | `architecture-decision-records` | ADR for tooling decisions |
| Docker patterns | `docker-containerization` | Multi-stage builds, compose |

---

## References

- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [Pydantic v2 Documentation](https://docs.pydantic.dev/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [typing module](https://docs.python.org/3/library/typing.html)
