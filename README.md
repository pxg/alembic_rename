First create your role and database:
CREATE USER snacks;
CREATE DATABASE snacks WITH OWNER snacks ENCODING 'UTF8';

To create the schema run:
python models.py
