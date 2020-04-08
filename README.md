# Blank Django project with Custom User app
## Content
* [Description](#description)
* [Download and run](#download-and-run)
* [How to rename project in Django](#how-to-rename-project)
* [Moving project to a fresh git repository](#moving-project-to-a-fresh-git-repository)

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
* run `makemigrations` from manage.py (or `makemigrations users` if makemigrations discovered no changes)
* run `migrate`

### How to rename project
**In Pycharm select root project folder and do rename/refactor with seraching bot for references and in comments and strings If done manually follow steps below**
* Change root folder name
* in settings.py:
  * change ROOT_URLCONF to ROOT_URLCONF = "**your_project_name**.urls'
  * change WSGI_APPLICATION to WSGI_APPLICATION = '**your_project_name**.wsgi.application'
* in manage.py change line 8 (os.environ.setdefault('DJANGO_SETTINGS_MODULE', '**your_project_name**.settings')
* in asgi.py change line 14 (os.environ.setdefault('DJANGO_SETTINGS_MODULE', '**your_project_name**.settings')
* in wsgi.py change line 14 (os.environ.setdefault('DJANGO_SETTINGS_MODULE', '**your_project_name**.settings')
* in the first lines of all above files change docstrings to reflect app name.

### Moving project to a fresh git repository
**To make sure git log doesn't contain any of this repo history follow below steps**
* in project folder run `rm -rf .git` (remove complete git folder from this repo)
* run `git init` (start fresh git repo)
* run `git add .` (add all files to repo)
* run `git commit -m "Initial commit"`
* create new empty repo and copy its url
* run `git remote add origin your_new_repo.url` (e.g. git@github.com:<YOUR ACCOUNT>/<YOUR NEW_REPOSITORY>.git)
* run `git push -u origin master` (or `git push -u --force origin master`)
* You should have this project as a new clean repo on your git
