# Ingestion Developer Guide

`platform/` is a self-contained [uv](https://docs.astral.sh/uv/) project. The installable/importable
package is named `obs_platform` (not `platform`, which would collide with Python's standard
library `platform` module).

## Layout

- `platform/pyproject.toml` — uv project manifest
- `platform/src/obs_platform/ingestion/core/ingestor.py` — shared `Ingestor` interface, `Market`/`Quote` types
- `platform/src/obs_platform/ingestion/polymarket/adapter.py` — `PolymarketIngestor`
- `platform/src/obs_platform/ingestion/kalshi/adapter.py` — `KalshiIngestor`
- `platform/src/obs_platform/{models,simulation,analytics,tools}/` — placeholder submodules
- `platform/tests/` — pytest suite

## Setup

```powershell
cd platform
uv sync
```

This creates `.venv/`, resolves `uv.lock`, and installs `obs_platform` in editable mode.

## Running tests

```powershell
uv run pytest
```

## Using the package

```powershell
uv run python -c "from obs_platform.ingestion.polymarket.adapter import PolymarketIngestor; print(PolymarketIngestor)"
```

```python
from obs_platform.ingestion.core.ingestor import Ingestor, Market, Quote
from obs_platform.ingestion.polymarket.adapter import PolymarketIngestor
from obs_platform.ingestion.kalshi.adapter import KalshiIngestor

ingestor = PolymarketIngestor()
markets = await ingestor.list_markets()
```

## Adding a dependency

```powershell
uv add httpx
uv add --dev pytest-asyncio
```

## Adding a new vendor adapter

1. Create `platform/src/obs_platform/ingestion/<vendor>/adapter.py` implementing `Ingestor`.
2. Add `platform/src/obs_platform/ingestion/<vendor>/__init__.py` re-exporting the class.
3. Add tests under `platform/tests/ingestion/`.
4. Add vendor API notes under `platform/docs/<vendor>.md`.
