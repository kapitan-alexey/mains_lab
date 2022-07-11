REST API service for mainslab

## Run Project
```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## API Endpoints

### files upload

*api/xls-clients/*

> POST method for uploading client_org.xlsx file with form-data option

*api/xls-bills/*

> POST method for uploading bills.xlsx file with form-data option</br>

### retrieve info</br>

*api/clients/*

> GET method for getting clients info

*api/bills/*

> GET method for getting all bills info

*api/bills/client/'client_name'/*

> GET method for getting bills info related to 'client_name' client

*api/bills/organization/'organization_name'/*

> GET method for getting bills info related to 'organization_name' organization

## Other

Please keep in mind that *settings.py* is almost untouched, SECRET_KEY is still inside and debug option still remains True as well

