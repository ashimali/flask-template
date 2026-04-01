# {{ cookiecutter.application_name }}

#### Prerequisites

1. Python 3.13+
2. [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Node.js 22+

#### Setup

    make init

This will sync dependencies, install pre-commit hooks, and build CSS.

#### Run locally

    uv run flask run

#### Run with Docker

    make serve

App available at http://localhost:5050

#### CSS

Build once:

    make css-build

Watch for changes during development:

    make css-watch
