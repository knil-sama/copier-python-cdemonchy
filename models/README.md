Shared model between services, didn't want to go into full hexagonal architecture here

# Requirement

Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

# Update dependencies

```bash
uv lock
```

# Test

```bash
uv run pytest
```

# Coverage

```bash
uv run pytest --cov=models
```