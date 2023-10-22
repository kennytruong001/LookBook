from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, Flask
#from .models import User
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import login_user, login_required, logout_user, current_user
import boto3 
import hashlib
import json

from website.helper import getConfigs

from ..models.user import User

from ..database import mongo

keys = getConfigs()
#user_bp = Blueprint('user_routes', __name__, url_prefix='/user')
auth = Blueprint('auth', __name__)

client = boto3.client('dynamodb')
table = boto3.resource('dynamodb', aws_access_key_id=keys["ACCESS_KEY_ID"],
                     aws_secret_access_key=keys["ACCESS_SECRET_KEY"]).Table("LookBook_Database")
                    


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json['user']
        password = request.json['pwd']
        sha256_pass = hashlib.sha256(password.encode())
        #userInfo = table.get_item(Key={"User":username})["Item"]
        userInfo = mongo.user_collection.find_one({"username": username})

        print(userInfo)
        #title = userInfo["Title"]
        #if sha256_pass.hexdigest() == userRecord[input_name].getPassword():
        if userInfo:
            if password == userInfo["password"]:
                user = username
                pwd = password
                return {user: username, pwd: password}
        #         if title == "User":
        #             return redirect(url_for('user_views.home', name=user))
        #         if title == "Customer":
        #             return redirect(url_for('customer_views.home', name=user))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    #return render_template("login.html")


@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #class_type = request.form.get('type')
        #first_name = request.form.get('firstname')
        #last_name = request.form.get('lastname')
        username = request.json['user']
        #email = request.form.get('email')
        password = request.json['pwd']
        #password2 = request.form.get('password2')
        #phone_number = request.form.get('phonenumber')

        #if len(username) < 4:
        #    flash('Username must be greater than 3 characters.', category='error')
        # if len(email) < 4:
        #     flash('Email must be greater than 3 characters.', category='error')
        # elif len(password1) < 7:
        #     flash('Password must be at least 7 characters.', category='error')
        # elif password1 != password2:
        #     flash('Passwords don\'t match.', category='error')
        # #elif len(phone_number) != 10:
        # #    flash('Invalid phone number.', category='error')
        # else:
        #     new_user = User(email=email, 
        #                     first_name=first_name, 
        #                     last_name=last_name,
        #                     password=hashlib.sha256(password1.encode())
        #                     #phone_number=phone_number
        #                     )
        # user_info = {
        #     "username":username,
        #     "password":password,
        #     "email": None,
        #     "first_name": None,
        #     "last_name": None,
        #     "schedule": None
        # }
        
        userID = User(username=username,password=password)

        #Add this feature:
        #Check if user exists in database (either after submission or constant)

        userFound = mongo.user_collection.find_one({"username": username})

        if userFound:
            flash('User already exist.', category='error')
        else:
            response = {"user": username, "pwd": password}
            #mongo.user_collection.insert_one(user_info)
            mongo.user_collection.insert_one(userID.__dict__)
            #flash('Account created!', category='success')
        #     if class_type == "user":
        #         return redirect(url_for('user_views.home'))
        #     else:
        #         return redirect(url_for('customer_views.home'))
        #     # if request.method=='POST':

        #     #     userInfo = table.get_item(Key={"User":user})["Item"]
        #     #     items = response['Items']
        #     #     name = items[0]['name']
        #     #     print(items[0]['password'])
        #     #     if password == items[0]['password']:
        #     #         return render_template("home.html",name = name)
    #redirect(url_for('user_views.home'))
    #return render_template("index.html")
    #return "Hello World"
    return response

@auth.route('/sign-up-u', methods=['GET', 'POST'])
def sign_up_u():
    if request.method == 'POST':
        class_type = request.form.get('type')
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        phone_number = request.form.get('phonenumber')

        if len(username) < 4:
            flash('Username must be greater than 3 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(phone_number) != 10:
            flash('Invalid phone number.', category='error')
        else:
            flash('Account created!', category='success')
            new_user = User(email=email, 
                            first_name=first_name, 
                            password=hashlib.sha256(password1.encode()), 
                            phone_number=phone_number
                            )
            
            table.put_item(new_user)
            #db.session.add(new_user)
            #db.session.commit()
            #login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('user_views.home'))
            # if request.method=='POST':

            #     userInfo = table.get_item(Key={"User":user})["Item"]
            #     items = response['Items']
            #     name = items[0]['name']
            #     print(items[0]['password'])
            #     if password == items[0]['password']:
            #         return render_template("home.html",name = name)
    return render_template("sign_up_u.html")


@auth.route('/sign-up-c', methods=['GET', 'POST'])
def sign_up_c():
    if request.method == 'POST':
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        phone_number = request.form.get('phonenumber')

        if len(username) < 4:
            flash('Username must be greater than 3 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(phone_number) != 10:
            flash('Invalid phone number.', category='error')
        else:
            flash('Account created!', category='success')
            new_user = User(email=email, 
                            first_name=first_name, 
                            password=hashlib.sha256(password1.encode()), 
                            phone_number=phone_number
                            )
            
            table.put_item(new_user)
            #db.session.add(new_user)
            #db.session.commit()
            #login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('customer_views.home'))
            # if request.method=='POST':

            #     userInfo = table.get_item(Key={"User":user})["Item"]
            #     items = response['Items']
            #     name = items[0]['name']
            #     print(items[0]['password'])
            #     if password == items[0]['password']:
            #         return render_template("home.html",name = name)
    return render_template("sign_u_c.html")

#f.close()