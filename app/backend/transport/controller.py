from flask import Blueprint

app = Blueprint('transport', __name__, url_prefix='/transport')

@app.get("/")
def get():
    return "Hello, World!"