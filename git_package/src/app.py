from flask import Flask


def create_app():
    print("creating app...")
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello World!"

    return app


def start_app(debug_mode: bool = True):
    app = create_app()
    print(f"app created: {app.name=}, starting...")
    app.run(port=0, debug=debug_mode)

