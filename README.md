# Jenn's Little Island Blog
Welcome to my little (Vancouver Island) blog!

### Getting Ready

I'm using Python 3.5.1, Django 1.9.4, and virtualenv. 

###In The Terminal

To get the proper python up and running (and using env, if you've already installed it: 
```bash
alias python=python3.5
source env/bin/activate
```

### Installing Packages

Run the following code to "bundle install" all the packages:

```bash
python3.5 -m pip install -r requirements.txt
```

###Set up the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

To run the server, type the following into your terminal:

```bash
python manage.py runserver
```

Go to localhost:8000 in your browser.
