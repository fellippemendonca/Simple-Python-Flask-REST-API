# Simple Python Flask REST API

## Instructions:
```bash
$ pip3 install -r requirements.txt
$ export FLASK_APP=app
$ flask run
```

## Requests

### GET Vehicles
```bash
curl --location --request GET 'http://127.0.0.1:5000/vehicles?sort=miles_until_service&make=Ford&model=Titanium&page=1&per_page=2' \
--header 'Authorization: Basic YWRtaW5pc3RyYXRvcjpwYXNzd29yZA=='
```

### GET Vehicles by ID
```bash
curl --location --request GET 'http://127.0.0.1:5000/vehicles/db99d2a1-6e5b-49dc-91f4-738caf09dcde' \
--header 'Authorization: Basic YWRtaW5pc3RyYXRvcjpwYXNzd29yZA=='
```

## Next steps:
- Dockerize
- Host on cloud