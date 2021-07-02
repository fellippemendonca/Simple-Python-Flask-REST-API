import pymongo
from db.fs import getVehicles

print('Connecting to MongoDB server...')
myclient = pymongo.MongoClient('mongodb://192.168.178.5:27017/')
mydb = myclient['kyte']
vehiclesCol = mydb['vehicles']


def dbSeed():
  checkData = vehiclesCol.find_one()
  if checkData == None:
    print('No data found in DB. Auto-fill will be done.')
    vehiclesCol.insert_many(getVehicles())
dbSeed()

def findVehicles(query, pages, sortValue):
  limitNum = pages['per_page']
  skipNum = pages['per_page'] * abs(pages['page'] - 1)
  fieldRules = { '_id': 0 }
  if sortValue:
    return [vehicle for vehicle in vehiclesCol.find(query, fieldRules).skip(skipNum).limit(limitNum).sort(sortValue)]
  return [vehicle for vehicle in vehiclesCol.find(query, fieldRules).skip(skipNum).limit(limitNum)]

def findVehicleById(vehicleId):
  fieldRules = { '_id': 0 }
  vehicle = vehiclesCol.find_one({ 'id': vehicleId }, fieldRules)
  return vehicle
