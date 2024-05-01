## Prequestits
You need an Postgresql Db up an running.
And you probably should take a look at https://github.com/HearthSim/dj-paypal/tree/main
```
sudo -u postgres psql
postgres=# create role paypal with login PASSWORD "secret" 
sudo apt-get install libpq-dev #for psycopg2
```


## Install:
```
cp .env.template .env
```
Set all the variables there.
```
python3 -m pip install poetry
poetry install
poetry run python3 manage.py migrate
```

## Start:
```
poetry run gunicorn main.wsgi
```
open a browser an go to:
```
localhost:8000/hello?name=yourname
```

to see greetings to you.
