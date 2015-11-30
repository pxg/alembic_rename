
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
CREATE USER snacks;
CREATE DATABASE snacks WITH OWNER snacks ENCODING 'UTF8';
```

To create the schema run:
python models.py
