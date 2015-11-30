Install the snacks package in editable mode:
```
pip install -e .
```

Install the requirements:
```
cd snacks
pip install -r requirements.txt
```

Create your role and database:
```
psql
CREATE USER snacks;
CREATE DATABASE snacks WITH OWNER snacks ENCODING 'UTF8';
```

Run the migrations to create the schama:
```
cd snacks
alembic -c alembic.ini upgrade head
```
