from dotenv import load_dotenv
from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

load_dotenv()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    register_errorhandlers(app)
    register_blueprints(app)
    register_extensions(app)
    return app


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, "code", 500)
        error_description = getattr(
            error, "description", "An unexpected error occurred."
        )
        return render_template(
            "error.html", code=error_code, message=error_description
        ), error_code

    app.errorhandler(HTTPException)(render_error)


def register_blueprints(app):
    from application.frontend.views import frontend

    app.register_blueprint(frontend)


def register_extensions(app):
    pass
