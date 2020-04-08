# Blank Django project with Custom User app
## Content
* [Description](#description)
* [Download and run](#download-and-run)

# Description
**This is a template Django project with extended User model:**

* deleted username field (email as authentication)
* custom password validators
* tests for user manager and password validators

# Download and run
**To run this project on Your computer follow these steps**
* clone this repository
* create virtualenvironment (run `virtualenv venv`)
* activate virtualenvironment (run `source venv/bin/activate`)
* install requirements (run `pip install -r requirements.txt` inside project repository)
* change User model so it suits your needs
* copy example_local_settings.py and change name to local_settings.py (conigure db and email backend if needed)
* change secret_key in local_settings.py
* if needed rename project [How to rename project in Django](#how-to-rename-project)
* run makemigrations from manage.py
* run migrate

# How to rename project
**In Pycharm select root project folder and do rename/refactor with seraching bot for references and in comments and strings If done manually follow steps below**
* Change root folder name
* in settings.py:
  * change ROOT_URLCONF to ROOT_URLCONF = "**your_project_name**.urls'
  * change WSGI_APPLICATION to WSGI_APPLICATION = '**your_project_name**.wsgi.application'
* in manage.py change line 8 (os.environ.setdefault('DJANGO_SETTINGS_MODULE', '**your_project_name**.settings')
* in asgi.py change line 14 (os.environ.setdefault('DJANGO_SETTINGS_MODULE', '**your_project_name**.settings')
* in wsgi.py change line 14 (os.environ.setdefault('DJANGO_SETTINGS_MODULE', '**your_project_name**.settings')
* in the first lines of all above files change docstrings to reflect app name.
