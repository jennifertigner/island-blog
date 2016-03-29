# Jenn's Little Island Blog
Welcome to my little (Vancouver Island) blog! py

## Getting Ready

### Python Installation
You should install Python v3.5.1. Run the following to check if it is installed (and to check which version):

```bash
python --version
```

### Virtualenv Installation

Virtualenv enables multiple side-by-side installations of Python, one for each project.

```bash
pip install virtualenv
```

Once you have virtualenv installed, just fire up a shell and create your own environment:

```bash
mkdir myproject
cd myproject
virtualenv env
```

Now, whenever you want to work on a project, you only have to activate the corresponding environment:

```bash
Unix Systems: source env/bin/activate
```

To exit the virtual environment:

```bash
deactivate
```

##While in virtualenv
### Installing Packages

After you have installed Python and Pip (or Virtual Env), run the following code to "bundle install" all the packages:

```bash
pip install -r requirements.txt
```

If you want to add any packages, do the following:

```bash
pip install pkg_name
pip freeze
```

  Copy exactly the line of the package you just installed from the Terminal into this requirements.txt

## Running the Project
###Set up the Database
```bash
python manage.py migrate
python manage.py migrate kepler_exoplanets
./manage.py generate_data
```

To run the server, type the following into your terminal:

```bash
python manage.py runserver
```

Go to localhost:8000 in your browser.

