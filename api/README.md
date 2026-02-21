Fatspi for the project

# Requirement

Install [uv](https://docs.astral.sh/uv/getting-started/installation/)  
Install [bruno](https://docs.usebruno.com/bruno-basics/download) or the [cli](https://docs.usebruno.com/bru-cli/installation)

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
uv run pytest --cov=api
```

# Integration test

Either import the integraton_tests folder as a Bruno workspace in the GUI of Bruno
or run the following with the cli

The API need to be running see [this](../README.md#run-docker)

```bash
cd integration_tests/collections/api
bru run --reporter-html results.html
```

