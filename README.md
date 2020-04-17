# DjangoWebApp
This project follows the tutorial of
[realpython website](https://realpython.com/get-started-with-django-1/)
to create an Django based web application. It will be the basis for a
follow-up project where I create my own web application which will
be hosted by my raspberry pie.

## Quickstart
Run the following code in your terminal to start the python virtual
environment _venvDWA_ :

```$ source venv/bin/activate```

The virtual environment will be active when the following is visible:

``` (venv) $ ```

To run the server:

```$ python manage.py runserver```

## Structure

 ```
 DjangoWebApp/
│
├── personal_portfolio/
│   ├── templates/
│   │   ├── base.html
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── venvDWA/
│
└── manage.py
│
└──projects
│   ├── __init__.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

* **_ _init__.py** tells Python to treat the directory as a Python package.
* **admin.py** contains settings for the Django admin pages.
* **apps.py** contains settings for the application configuration.
* **models.py** contains a series of classes that Django’s ORM converts to
database tables.
* **tests.py** contains test classes.
* **views.py** contains functions and classes that handle what data is displayed
in the HTML templates.


## Dependencies
The following packages are used:
* Django

## Known Bugs
The project just started, here is work to be done.
