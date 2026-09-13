# Platform

Application workspace for the production-oriented platform code that supports Observatory research workflows.

This is a self-contained [uv](https://docs.astral.sh/uv/) project. The root importable package is
`obs_platform` (source at `src/obs_platform/`), organized as submodules — see `platform/docs/ingestion.md`
for setup and import instructions.

## Subdirectories
- `src/obs_platform/ingestion/`: Data collection and import pipelines (Polymarket, Kalshi adapters).
- `src/obs_platform/analytics/`: Analytical services and processing logic.
- `src/obs_platform/simulation/`: Scenario and simulation engines.
- `src/obs_platform/models/`: Shared model implementations and artifacts.
- `src/obs_platform/tools/`: Developer and operational support utilities.
- `tests/`: pytest suite.
- `docs/`: developer-facing documentation (ingestion guide, vendor API notes).

## Quickstart

```powershell
cd platform
uv sync
uv run pytest
```
