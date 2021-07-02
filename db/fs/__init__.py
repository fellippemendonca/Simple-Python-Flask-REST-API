import json

with open("vehicle_data.json") as jsonFile:
  jsonObject = json.load(jsonFile)
  jsonFile.close()

def getVehicles():
  return jsonObject