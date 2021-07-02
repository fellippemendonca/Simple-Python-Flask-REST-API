from flask import jsonify, make_response
from  db.mongodb import orm
from server.controllers.helpers import exctractPage
from server.controllers.vehicles.helpers import exctractVehicleQuery


def find(args):
  query = exctractVehicleQuery(args)
  pages = exctractPage(args)
  sortValue = args.get('sort')
  try:
    vehicles = orm.findVehicles(query, pages, sortValue)
    return jsonify({ 'data': vehicles })
  except:
    return make_response(jsonify({'error': 'Not found'}), 404)
  

def findById(vehicleId):
  try:
    vehicle = orm.findVehicleById(vehicleId)
    return jsonify({ 'data': vehicle })
  except:
    return make_response(jsonify({'error': 'Not found'}), 404)
