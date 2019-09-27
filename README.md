# Django OAuth Client Example
A Client application written in django with django-allauth that consumes the resources on OAuth Server

This is a djano application I created to showcase how to implement OAuth2 authentication on a web application using django-allauth.


The associated OAuth2 Server for this client can be found [here](https://github.com/faisallarai/django-oauth-server.git).

# Demo
```
(https://django-oauth-client.herokuapp.com)
```

# Host Requirements
```
Macbook / Linux
Python3
Pip
Virtualenv
```

# To run the application first clone the repository
```
git clone https://github.com/faisallarai/django-oauth-client.git
```

# Move into directory
```
cd django-oauth-client
```

# Install the dependencies
```
Virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 
```

# Run migration
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Run server
```
python manage.py runserver
```

The application should be running at (http://localhost:8000/)

