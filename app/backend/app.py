from flask import Flask, json
from transport.controller import app as transport_app

def create_app():
    app = Flask(__name__)
    json.provider.DefaultJSONProvider.ensure_ascii = False
    

    app.register_blueprint(transport_app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, port=3000)