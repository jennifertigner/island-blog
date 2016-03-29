# Jenn's Little Island Blog
Welcome to my little (Vancouver Island) blog!

### Getting Ready

I'm using Python 3.5.1, Django 1.9.4, and virtualenv. 

### Installing Packages

Run the following code to "bundle install" all the packages:

```bash
pip install -r requirements.txt
```

###Set up the Database
```bash
python manage.py migrate
python manage.py migrate blog
```

To run the server, type the following into your terminal:

```bash
python manage.py runserver
```

Go to localhost:8000 in your browser.
