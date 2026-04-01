# flask-template

A [Copier](https://copier.readthedocs.io/en/stable/) template for Flask applications.

## Prerequisites

1. Python 3.13+
2. [uv](https://docs.astral.sh/uv/getting-started/installation/)

## How to use it

Run:

    uvx copier copy gh:ashimali/flask-cookiecutter my-app

You will be prompted for an application name and GitHub username. Copier will create a directory with your project scaffolded out.

Then cd into the new directory and run:

    make init

This will sync dependencies, install pre-commit hooks, and build CSS.

## Updating an existing project

When the template is updated, pull changes into your project:

    cd my-app
    uvx copier update

## What's in the generated project

- Flask with application factory pattern
- SQLAlchemy + PostgreSQL
- Tailwind CSS + DaisyUI
- Docker Compose dev environment
- pytest, ruff, pre-commit
- uv for dependency management

Run with Docker:

    make serve

App available at http://localhost:5050

## Developing this template

    make init     # install pre-commit hooks
    make lint     # run linters across all files
