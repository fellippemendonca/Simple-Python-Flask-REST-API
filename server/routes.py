from flask import jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
from server import middleware
from server.controllers import vehicles


def init(app):
  auth = middleware.init()

  @app.route('/vehicles', methods=['GET'])
  @auth.login_required
  def find():
    return vehicles.find(request.args)

  @app.route('/vehicles/<vehicle_id>', methods=['GET'])
  @auth.login_required
  def findById(vehicle_id):
    return vehicles.findById(vehicle_id)

  @app.errorhandler(404)
  def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
