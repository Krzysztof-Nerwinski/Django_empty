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
* change SECRET_KEY
* change User model so it suits your needs
* copy example_local_settings.py and change name to local_settings.py (conigure db and email backend if needed)
* change secret_key in local_settings.py
* run makemigrations from manage.py
* run migrate
