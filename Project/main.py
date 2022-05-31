import logging

from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
import json
from . import db
from .models import JsonData
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route("/getjson")
@login_required
def get_json():
    return render_template("add_json.html")

@main.route("/getjson", methods=['POST'])
@login_required
def post_data():
    logging.info("JSON Post data request initiated")
    # if file is not json then display flash msg and reload page
    # if json file then store it to database
    if request.files:
        json_file = request.files['jsonfile']
        # import pdb;pdb.set_trace()
        if json_file.filename == '' or json_file.filename.split(".")[1] != 'json':
            flash("Enter the correct file format.")
            return redirect(url_for('main.post_data'))
        json_file_array = json.load(json_file)
        for i in range(len(json_file_array)):
            data = json_file_array[i]
            userId = data.get('userId', "NA")
            id = data.get('id', "NA")
            title = data.get('title', "NA")
            body = data.get('body', "NA")

            data = JsonData.query.filter_by(
                id=id).first()  # if this returns a user, then the email already exists in database

            if data:  # if a user is found, we want to redirect back to signup page so user can try again

                if i == len(json_file_array)-1:
                    flash('Data already present in database, please use new data.')
                    return redirect(url_for('main.post_data'))
                continue

            # create a new json with the form data.
            new_json_data = JsonData(userId=userId, id=id, title=title, body=body)

            # add the new user to the database
            db.session.add(new_json_data)
            db.session.commit()
        return redirect(url_for('main.profile'))



@main.route("/showjson")
@login_required
def show_json():
    json_data = JsonData.query.filter_by().all()
    lst = []
    for data in json_data:
        one_dict = {"id":data.id, "title": data.title, "body":data.body}
        lst.append(one_dict)
    return render_template('view_json.html', json_data=lst)
