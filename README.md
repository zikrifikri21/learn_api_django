(optional)
exit project and create environment


## Create environment
```bash
py -m env you_env
```
*** activate environment ***
```bash
.\you_env\Scripts\activate
```
## Install requirements
```bash
pip -m install ./myapi/requirements.txt
```

### .env
```bash
APP_NAME="My API"
DEBUG=True
SECRET_KEY='django-insecure-'

#DATABASE
DB_ENGINE=django.db.backends.postgresql
DB_NAME=django
DB_USER=postgres
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

### migrate database


