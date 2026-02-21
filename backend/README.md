Backend that handle most of the work

# Requirement

Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Update dependencies

```bash
uv lock
```

# Test

```bash
uv run pytest
```

# Coverage

```bash
uv run pytest --cov=backend
```