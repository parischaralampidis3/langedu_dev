activate an env
---------------

python -m venv lang

cd Scripts

./activate


install Django
--------------

python -m pip install django

(.venv) $ django-admin startproject <project-name>

python manage.py startapp <appname>

installed Postgress
-------------------
database is pointed at settings.py
----------------------------------


1. Change models.py
2. python manage.py makemigrations
3. python manage.py migrat

. Where to Look in pgAdmin (Very Common Gotcha)

Even after migrating, pgAdmin does not auto-refresh.

Don't drop tables manually from UI

Do this in pgAdmin:

Expand:

Servers
  → PostgreSQL
    → Databases
      → dev_langedu
        → Schemas
          → public
            → Tables


Right-click “Tables” → Refresh


Notes
-----

Build a modular Django monolith with PostgreSQL, MTV architecture, and a thin service layer.
Ship the MVP.
Then evolve — don’t over-architect now.

Never let a core entity exist without an owner (organization).

MVC
---
Define models

-Course


Database
--------

CREATE USER languser_dev WITH PASSWORD 'languser_dev';


ALTER ROLE languser_dev SET client_encoding TO 'utf8';
ALTER ROLE languser_dev SET default_transaction_isolation TO 'read committed';
ALTER ROLE languser_dev SET timezone TO 'UTC';


