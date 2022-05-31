## Read JSON data which is given by user, and needs to signup and login first before adding data.

In this project I use:
- Use the Flask-Login library for session management
- Use the built-in Flask utility for hashing passwords
- Add protected pages to the app for logged-in users only
- Use Flask-SQLAlchemy to create a User and JsonData model
- Create sign-up and login forms for the users to create accounts and log in
- Flash error messages back to users when something goes wrong
- Use information from the user’s account to display on the profile page


## Folder structure
```bash
.
├── auth                        #virtual environment
├── Project                     # Main Directory
│   ├── templates               # HTML Template content
│   │   │──base.html
│   │   │──login.html
│   │   │──signup.html
│   │   │──profile.html
│   │   │──view_json.html
│   │   │──add_json.html
│   ├── auth.py
│   ├── main.py
│   ├── __init__.py
│   ├── models.py
│   └── ... 
└── ...
```

----
### Step 1- Create directory
```
mkdir Flask_login_auth
```
### Step 2- Create virtual env in that directory
```commandline
python -m venv auth
source auth/bin/activate
```
After creating virtual environment add all the required libraries from `requirements.txt` file.
```commandline
pip install -r requirements.txt
```
### Step 3- Install required packages in *auth* virtual env
```commandline
pip install flask flask-sqlalchemy flask-login
```
### Step 4- Create main file app
__init__.py --> In this file we have two blueprint (one for auth and second for other purpose)
### Step 5 — Adding Routes
Add routes in auth.py and main.py according to their blueprint
After adding routes check this app by running the server, for that we have to use below commands
```commandline
export FLASK_APP=Project
export FLASK_DEBUG=1
flask run -> from main directory
Goto - localhost:5000/profile
```
---
### Step 6 — Creating Templates
create all the required templates and store it in templates folder

---
### Step 7 — Creating User Models
Model is nothing but the schema of database table.
Whatever fields we add into Model class that will represent as a table fields.

Models created in Flask-SQLAlchemy are represented by classes that then translate to tables in a database. The attributes of those classes then turn into columns for those tables.

---
### Step 8 — Configuring the Database
Use below command in terminal or run `create_db.py` file
```commandline
from project import db, create_app, models
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```
---

### Step 9 — Protecting Pages
`@login_requried` use this decorator from Flask-Login to protect the data from user who is not logged in into the system.

If the user is not logged in, the user will get redirected to the login page, per the Flask-Login configuration.

The routes which has `@login_required` decorator, you can use the `current_user` object inside the function.
This `current_user` represents the user from the database and provides access all the attributes of that user with dot notation. For example, `current_user.email`, `current_user.password`, and `current_user.name`, and` current_user.id` will return the actual values stored in the database for the logged-in user.

----

# Conclusion
In this Project, I used Flask-Login and Flask-SQLAlchemy to build a login system for an app. I covered how to authenticate a user by first creating a user model and storing the user information. Then I had to verify the user’s password was correct by hashing the password from the form and comparing it to the one stored in the database. Finally, I added authorization to the app by using the `@login_required` decorator on a profile page so only logged-in users can see that page. After login, you can upload json file and then code will check the data given in Json file is already present in database or not.

---
