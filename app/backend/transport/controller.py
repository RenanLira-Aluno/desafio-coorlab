from flask import Blueprint, jsonify, request
from transport.service import TransportService

app = Blueprint('transport', __name__, url_prefix='/transport')

service = TransportService()

@app.get("/")
def index():
    return service.get_all()

@app.get("/comfortable-or-economic")
def getComfortableOrEconomic():

    city = request.args.get('city')
    date = request.args.get('date')

    

    return service.getComfortableOrEconomic(city)

