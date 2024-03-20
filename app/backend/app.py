from flask import Flask, json, jsonify
from transport.controller import app as transport_app
from transport.exceptions.queryException import QueryException

def create_app():
    app = Flask(__name__)
    json.provider.DefaultJSONProvider.ensure_ascii = False
    

    app.register_blueprint(transport_app)

    @app.errorhandler(QueryException)
    def handle_query_exception(error):
    
        return jsonify({"error": error.message}), error.code

    return app


if __name__ == '__main__':
    create_app().run(debug=True, port=3000)