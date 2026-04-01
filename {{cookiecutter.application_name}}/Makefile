init::
	git init
	uv sync
	uv run pre-commit install
	npm install
	npm run css:build

upgrade::
	uv lock --upgrade
	uv sync
	npm install
	npm run css:build

css-build::
	npm run css:build

css-watch::
	npm run css:watch

serve::
	docker compose up --build
