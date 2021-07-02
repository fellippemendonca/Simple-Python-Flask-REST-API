def exctractPage(args):
  obj = {}
  if args.get('page'):
    obj['page'] = int(args.get('page'))
  else:
    obj['page'] = 1

  if args.get('per_page'):
    obj['per_page'] = int(args.get('per_page'))
  else: 
    obj['per_page'] = 20

  return obj