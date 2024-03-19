from flask import Blueprint
from transport.service import TransportService

app = Blueprint('transport', __name__, url_prefix='/transport')

service = TransportService()

@app.get("/")
def index():
    return service.get_all()