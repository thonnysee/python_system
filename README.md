# Python Project 
## Cero y Uno Development and <<hidalgo.lab>> 
### Description
Using the knowledge of the python training create a project.

This project is based on a diagram made in class and my choice was a Shop system (POS) and if there is time to continue to start on making the start of administrations modules trying to throw high to get a close start on a ERP.

The shop will be base on this module at first glance and it will be modified:

[Diagram of project](https://drive.google.com/file/d/1Hd7CK6-ECtQGTks6K1F8NTuYsUobYb4Z)


Models
  * Users
  * Products
  * Orders
  * Cart
  * CartItems
  * Catgeories 
  * OrderItems
  * TODO: Define next models to be used

[Models Diagram](https://app.sqldbm.com/PostgreSQL/Share/Mh7vbDDSIZRJvCgKvRJ0-UGFrngIE8md_DYjF4jNYw0)

# Python Shop setup

**Setting Up Containers for Django Project**

1. Build DB container: `>docker-compose build db`
1. Bring DB container up: `>docker-compose up db`
    1. Set DB container to run on background:  `>docker-compose up -d db`
1. Build MIGRATIONS container: `>docker-compose build migration`
1. Build WEB container: `>docker-compose build web`
1. Create a Django Project: `>docker-compose run web django-admin startproject my_web`
1. Setup DB connection on settings.py file
1. Run MIGRATIONS container to create db `>docker-compose up migration`
1. Run Web container to check if settings and db are working: `>docker-compose up web`
1. Create a Super User for Admin: `>docker-compose run web python manage.py createsuperuser`

**Helpfull Commands**
1. Create migrations for a specific app: `>docker-compose run migration python manage.py makemigrations <APP_NAME>`



## Version
0.2
## Credits

- [Antonio Carbajal][carbajalgalindo@gmail.com]
