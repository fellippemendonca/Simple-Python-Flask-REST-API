def exctractVehicleQuery(args):
  obj = {}
  if args.get('make'):
    obj['make'] = args.get('make')
  if args.get('model'):
    obj['model'] = args.get('model')
  if args.get('status'):
    obj['status'] = args.get('status')
  if args.get('vehicle_class'):
    obj['vehicle_class'] = args.get('vehicle_class')
  if args.get('license_plate_number'):
    obj['license_plate_number'] = args.get('license_plate_number')
  if args.get('license_plate_state'):
    obj['license_plate_state'] = args.get('license_plate_state')
  return obj
