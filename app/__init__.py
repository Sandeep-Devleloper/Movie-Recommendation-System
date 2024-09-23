from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static")  # Keep the static folder argument
    
    # Import and register the blueprint from routes
    from .routes import main
    app.register_blueprint(main)
    
    return app
