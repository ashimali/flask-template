# flask-template

A [Copier](https://copier.readthedocs.io/en/stable/) template for Flask applications.

## Prerequisites

1. Python 3.14+
2. [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. [just](https://just.systems/man/en/installation.html)

## How to use it

Run:

    uvx copier copy gh:ashimali/flask-cookiecutter my-app

You will be prompted for an application name and GitHub username. Copier will create a directory with your project scaffolded out.

Then cd into the new directory and run:

    just init

This will sync dependencies, install pre-commit hooks, and build CSS.

## Updating an existing project

When the template is updated, pull changes into your project:

    cd my-app
    uvx copier update

## What's in the generated project

- Flask with application factory pattern
- SQLAlchemy + PostgreSQL
- Pico CSS
- Docker Compose dev environment
- pytest, ruff, pre-commit
- uv for dependency management

No frontend build needed

Run with Docker:

    just serve

App available at http://localhost:5050

## Developing this template

    just init     # install pre-commit hooks
    just lint     # run linters across all files


#TODO - test updates
