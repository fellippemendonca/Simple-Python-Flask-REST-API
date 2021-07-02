from flask import jsonify
from  db.mongodb import orm
from server.controllers.helpers import exctractPage
from server.controllers.vehicles.helpers import exctractVehicleQuery


def find(args):
  query = exctractVehicleQuery(args)
  pages = exctractPage(args)
  sortValue = args.get('sort')
  return jsonify({ 'data': orm.findVehicles(query, pages, sortValue) })

def findById(vehicleId):
  vehicle = orm.findVehicleById(vehicleId)
  return jsonify({ 'data': vehicle })
