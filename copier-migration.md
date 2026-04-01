# Cookiecutter to Copier Migration

## Overview

Migrate this project from a cookiecutter template to a [Copier](https://copier.readthedocs.io/en/stable/) template. The main structural differences are:

- `cookiecutter.json` becomes `copier.yml`
- Template files live in a `template/` subdirectory (configured via `_subdirectory`)
- Variables drop the `cookiecutter.` prefix (`{{cookiecutter.application_name}}` becomes `{{application_name}}`)
- Only files with a `.jinja` suffix are rendered through Jinja2 (others copy as-is)
- Hooks move from `hooks/` scripts to `_tasks` in `copier.yml`
- Copier supports `copier update` for pulling template changes into existing projects

## Steps

### 1. Create `copier.yml`

Replace `cookiecutter.json` with `copier.yml` at the project root:

```yaml
_subdirectory: template

_templates_suffix: .jinja

application_name:
  type: str
  help: Name of the application

github_name:
  type: str
  help: Github user or organisation name

_tasks:
  - command: echo "Run 'make init' to set up the project"
```

Then delete `cookiecutter.json`.

### 2. Restructure the directory layout

Move the template directory into a `template/` subdirectory and drop the `cookiecutter.` prefix from the directory name:

```bash
mkdir template
mv '{{cookiecutter.application_name}}' 'template/{{application_name}}'
```

Delete the `hooks/` directory (its logic is now in `_tasks` above):

```bash
rm -rf hooks
```

### 3. Rename variable references in files

In every file that references `cookiecutter.application_name`, replace with just `application_name`. These are the affected files:

| File | What to change |
|------|----------------|
| `pyproject.toml` | `{{cookiecutter.application_name}}` on line 2 |
| `README.md` | `{{ cookiecutter.application_name }}` on line 1 |
| `LICENSE` | `{{ cookiecutter.application_name }}` on line 3 |
| `application/templates/base.html` | Two occurrences on lines 9 and 14 |

### 4. Add `.jinja` suffix to files that need rendering

Only files with a `.jinja` extension will be processed by Copier's Jinja2 engine. Rename the files that contain template variables:

```bash
cd template/'{{application_name}}'
mv pyproject.toml pyproject.toml.jinja
mv README.md README.md.jinja
mv LICENSE LICENSE.jinja
mv application/templates/base.html application/templates/base.html.jinja
```

All other files (Python, Docker, Makefile, HTML templates, etc.) copy verbatim without rendering.

### 5. Remove `{% raw %}` / `{% endraw %}` from non-rendered HTML templates

These files no longer need raw blocks because they won't have the `.jinja` suffix and won't be processed by Copier at all:

- `application/templates/index.html` - remove `{% raw %}` (line 1) and `{% endraw %}` (line 6)
- `application/templates/401.html` - same pattern
- `application/templates/404.html` - same pattern
- `application/templates/500.html` - same pattern

The Flask Jinja2 syntax in these files will pass through untouched.

### 6. Fix `base.html.jinja`

This file is trickier because it contains both Copier variables (`{{application_name}}`) and Flask Jinja2 syntax (`{{ url_for() }}`, `{% block %}`, etc.). The `{% raw %}` blocks need to stay to protect the Flask syntax, but the variable references need updating.

Change the two `cookiecutter.application_name` references to `application_name`:

```html
{% raw %}
<!doctype html>
...
  <title>{% block title %}{% endraw %}{{ application_name }}{% raw %}{% endblock %}</title>
...
    <h1 ...><a href="/">{% block titlebar_service %}{% endraw %}{{ application_name }}{% raw %}{% endblock %}</a></h1>
...
{% endraw %}
```

### 7. Add the Copier answers file

Create `template/{{application_name}}/.copier-answers.yml.jinja`:

```yaml
# Changes here will be overwritten by Copier
{{ _copier_answers|to_nice_yaml }}
```

This file records the answers used during generation. It gets committed into generated projects and enables `copier update` to pull in template changes later.

### 8. Tag a release

Copier uses Git tags for versioning. Tag the initial release after committing everything:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## Final directory structure

```
flask-cookiecutter/
├── copier.yml
├── README.md
└── template/
    └── {{application_name}}/
        ├── .copier-answers.yml.jinja
        ├── .dockerignore
        ├── .flaskenv
        ├── .gitignore
        ├── .node-version
        ├── .pre-commit-config.yaml
        ├── .python-version
        ├── application/
        │   ├── __init__.py
        │   ├── config.py
        │   ├── extensions.py
        │   ├── factory.py
        │   ├── frontend/
        │   │   ├── __init__.py
        │   │   └── views.py
        │   ├── models.py
        │   ├── static/css/input.css
        │   ├── templates/
        │   │   ├── 401.html          (no .jinja - plain Flask templates)
        │   │   ├── 404.html
        │   │   ├── 500.html
        │   │   ├── base.html.jinja   (has .jinja - contains Copier variables)
        │   │   └── index.html
        │   └── wsgi.py
        ├── compose.yaml
        ├── docker/Dockerfile.dev
        ├── LICENSE.jinja
        ├── Makefile
        ├── package.json
        ├── Procfile
        ├── pyproject.toml.jinja
        ├── README.md.jinja
        └── tests/__init__.py
```

## Usage changes

```bash
# Before (cookiecutter)
cookiecutter gh:user/flask-cookiecutter

# After (copier)
copier copy gh:user/flask-cookiecutter my-project

# Updating an existing project when the template changes (new capability)
cd my-project
copier update
```
