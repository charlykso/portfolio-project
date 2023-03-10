#!/usr/bin/python3
"""This is for the buy page"""

import os
import uuid
import datetime
from hashlib import md5
import json, requests
from models import storage
from models.user import User
from models.property import Property
from models.property_img import Property_img
# from models.address import Address
# from os import environ
from flask import Flask, request, render_template,\
    redirect, url_for, session
from web_dynamic.collective.checkEmail import CheckEmail
# from api.v1.app import close_db


app = Flask(__name__)
app.secret_key = 'ABCabcDEFdef123456'

@app.teardown_appcontext
def close_db(error):
    """Remove the current sqlalchemy session"""
    storage.close()


@app.route("/", strict_slashes=False)
def index():
    """landing page"""
    return render_template("index.html", cache_id=uuid.uuid4)


@app.route("/signup", methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """signup page"""
    msg=""
    if request.method == 'POST':
        
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone_no = request.form['phone_no']
        gender = request.form['gender']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not lastname or not firstname or\
            not email or not password or\
                not confirm_password or not phone_no\
                    or not gender:
            msg = "Please fill all required detail"
            return render_template("signup.html", msg=msg)
        elif len(password) < 6:
            msg = "Password must me be greater 5"
            return render_template("signup.html", msg=msg)
        elif password != confirm_password:
            msg = "Password did not match"
            return render_template("signup.html", msg=msg)
        elif CheckEmail.emailExists(email):
            msg = "Email already exist"
            return render_template("signup.html", msg=msg)

        url = "http://127.0.0.1:5003/api/v1/users"
        res = requests.post(url, json = {
            "firstname": firstname,\
                "lastname": lastname,\
                "phone_no": phone_no,\
                "email": email,\
                "password": password,\
                "gender": gender
        })
        if res.status_code != 201:
            msg= res.status_code
            return render_template("signup.html", msg=msg)

        session['loggedin'] = True
        session['id'] = res.json()['id']
        session['firstname'] = res.json()['firstname']
        session['lastname'] = res.json()['lastname']
        session['email'] = res.json()['email']
        session['cache_id'] = uuid.uuid4()
        msg = 'Logged in successfully !'
        print(res.json()['id'])   
        return redirect(url_for("index", 
                                msg=msg,
                                cache_id=uuid.uuid4()
                                ))

    msg = "Method not accepted"
    return render_template("signup.html", msg=msg)


@app.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    """login page"""
    msg=""
    email = request.form.get('email')
    password = request.form.get('password')
    if request.method == "POST":
        if not email or not password:
            msg = "Please fill in correctly"
            return render_template('login.html', msg=msg)
        users = storage.all(User)
        for value in users.values():
            if email == value.email and\
                value.password == md5(password.encode()).hexdigest():
                session['loggedin'] = True
                session['id'] = value.id
                session['firstname'] = value.firstname
                session['lastname'] = value.lastname
                session['email'] = email
                session['cache_id'] = uuid.uuid4()
                msg = 'Logged in successfully !'

                return redirect(url_for("index", msg=msg))

        msg = "Incorrect email or password"
    return render_template("login.html", msg=msg)


@app.route("/properties", strict_slashes=False)
def property():
    """List all the users"""
    return render_template("testbase.html",
                           cache_id=uuid.uuid4())

@app.route("/buy", strict_slashes=False)
def buy():
    """List of all properties"""
    properties = storage.all(Property).values()
    properties = sorted(properties, key=lambda k: k.description)
    for val in properties:
        for inval in val.property_imgs:
            print(inval.img_path)
    return render_template("buy.html",
                           properties=properties,
                           cache_id=uuid.uuid4())

@app.route("/details/<property_id>", strict_slashes=False)
def single_property(property_id):
    """Get the details of one property"""
    return render_template("details.html", cache_id=uuid.uuid4)


@app.route("/sell", methods=['GET', 'POST'], strict_slashes=False)
def sell():
    """sell page"""
    msg=""
    err_msg = ""
    if session['id']:
        user_id = session['id']
    if request.method == "POST":
        gen_property_id = request.form['gen_property_id']
        type = request.form['type']
        status = request.form['status']
        price = request.form['price']
        user_id = request.form['user_id']
        landmark = request.form['landmark']
        state = request.form['state']
        description = request.form['description']
        availability = "For Sale"

        if not gen_property_id or not type or not status or\
            not price or not user_id or not landmark or not state or\
                not description or not availability:
                    err_msg = "Please fill the required feilds"
                    return render_template("sell.html",
                                           err_msg=err_msg)

        url = "http://127.0.0.1:5003/api/v1/users/{}/properties".format(user_id)
        res = requests.post(url, json = {
            "user_id": user_id,\
            "gen_property_id": gen_property_id,\
            "status": status,\
            "type": type,\
            "landmark": landmark,\
            "state": state,\
            "price": price,\
            "description": description,\
            "availability": availability
        })

        if res.status_code != 201:
            err_msg= res.status_code
            return render_template("sell.html", err_msg=msg)

        msg = "Property created successfully"
        return render_template("sell.html", msg=msg)
    user = storage.get(User, user_id)
    new_list = []
    for property in user.properties:
        new_list.append(property)
    return render_template("sell.html", property=new_list)


@app.route("/uploadImage", methods=['POST'], strict_slashes=False)
def uploadImages():
    """for property image upload"""
    filepath = 'web_dynamic/static/images/property_images/{}'
    if request.method == "POST":
        if request.files is not None:
            for image in request.files:
                
                print(request.files[image].filename)
                print(request.form['property_id'])
                item = request.files[image].filename
                request.files[image].save(filepath.format(item))
                date = datetime.datetime.now()

                """getting the image extension"""
                file_tup = os.path.splitext(item)
                file_ext = file_tup[1]

                
                src = filepath.format(item)
                dest = filepath.format(date)
                dest = dest.strip(".,-")\
                    .replace(" ", "").replace(":", "_").replace(".", "_")
                img_dest = dest+file_ext

                """renaming the file"""
                os.rename(src, img_dest)

                x = {
                    "img_path" : img_dest,
                    "property_img": request.form["property_id"]
                }
                y = json.dumps(x)
                
                singleImage = Property_img(y)
                singleImage.property_id = request.form['property_id']
                singleImage.img_path = img_dest
                
                print(singleImage)
                singleImage.save()
                
            msg = "Uploaded successfully"
            return redirect(url_for("sell"), msg=msg)
        
        msg = "Uploaded successfully"
        return redirect(url_for("sell"), msg=msg)
        # print(request.form)

    return redirect(url_for("sell"))


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('firstname', None)
    session.pop('lastname', None)
    session.pop('email', None)
    session.pop('cache_id', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5002, debug=True)
    