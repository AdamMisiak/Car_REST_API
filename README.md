# Car REST API

Simple REST API created for practice purpose. Basic CRUD implemented using Django REST Framework.


## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [Tests](#tests)
* [Contact](#contact)

## Technologies
* Python version: 3.7
* Django version: 3.1.1
* DRF version: 3.11.1

## Setup
To create virtual environment:
```
python3 -m venv venv
```

To install requirements:
```
pip install -r requirements.txt
```

To migrate database:
```
python manage.py migrate
```

To create superuser:
```
python manage.py createsuperuser
```

## Commands

To run app locally:
```
python manage.py runserver     
```

To list all objects or add new object:
```
http://127.0.0.1:8000/cars/   
```

To detail specified object by id:
```
http://127.0.0.1:8000/cars/<id>
```

To delete specified object by brand or model:
```
http://127.0.0.1:8000/cars/?q=<brand_or_model>
```

To change format of display (api or json):
```
http://127.0.0.1:8000/cars/?format=<format>
```

## Tests

To run tests:
```
python manage.py test
```

## Contact
Created by Adam Misiak
