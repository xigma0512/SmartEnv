from flask import Flask

def create_app():
    app = Flask(__name__)

    from .index import index_bp
    from .api import api_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app