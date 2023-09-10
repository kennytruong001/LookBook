from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
#import key_config as keys
import boto3 
import hashlib
import json

from ..models.user import User

user_bp = Blueprint('user_routes', __name__, url_prefix='/user')
f = open('config.json')
secret = json.load(f)

client = boto3.client('dynamodb')
table = boto3.resource('dynamodb', aws_access_key_id=secret["ACCESS_KEY_ID"],
                     aws_secret_access_key=secret["ACCESS_SECRET_KEY"]).Table("LookBook_Database")
                    


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        sha256_pass = hashlib.sha256(password.encode())
        userInfo = table.get_item(Key={"User":user})["Item"]
        #if sha256_pass.hexdigest() == userRecord[input_name].getPassword():
        if userInfo:
            if password == userInfo["Password"]:
                return redirect(url_for('views.home', name=user))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html")


@user_bp.route('/logout')
def logout():
    return redirect(url_for('auth.login'))


@user_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
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
            # if request.method=='POST':

            #     userInfo = table.get_item(Key={"User":user})["Item"]
            #     items = response['Items']
            #     name = items[0]['name']
            #     print(items[0]['password'])
            #     if password == items[0]['password']:
            #         return render_template("home.html",name = name)
    return render_template("sign_up.html")

@user_bp.route('/get', methods=['GET'])
def get_user():
    """Get user by user id."""
    payload = request.get_json(force=True)
    id = payload.get("user_id", None)
    if not id:
        return jsonify({"error": "no button id found"})
    button = button_dao.get_button_by_id(id)
    if not button:
        return jsonify({'buton_id': id, "error": "no button id found"})
    return jsonify({
        'user_id': button.id,
        'button_count': button.count,
        'create_date': button.create_date,
        'update_date': button.update_date
    })

#f.close()