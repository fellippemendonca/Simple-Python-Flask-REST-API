#!flask/bin/python
import db.mongodb.orm
from flask import Flask
from server import routes


app = Flask(__name__)

routes.init(app)

if __name__ == '__main__':
  app.run(debug=True)
