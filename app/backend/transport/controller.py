from flask import Blueprint, jsonify, request
from transport.service import TransportService
from transport.exception.queryException import QueryException

app = Blueprint('transport', __name__, url_prefix='/transport')

service = TransportService()

@app.get("/")
def index():
    return service.get_all()

@app.get("/comfortable-or-economic")
def getComfortableOrEconomic():

    city = request.args.get('city')
    date = request.args.get('date')

    if not city or not date:
        raise QueryException(400, city=city, date=date)

    return service.getComfortableOrEconomic(city)

