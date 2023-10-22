from flask import Blueprint, render_template, request, flash, jsonify, session
import json
import boto3
from ..helper import getConfigs

configs = getConfigs()

client = boto3.client('dynamodb')
table = boto3.resource('dynamodb', aws_access_key_id=configs["ACCESS_KEY_ID"],
                    aws_secret_access_key=configs["ACCESS_SECRET_KEY"]).Table("CryptoTrader")

user_views = Blueprint('user_views', __name__)

@user_views.route('/', methods=['GET', 'POST'])
def home():
    #user = request.args.get('name')
    #userInfo = table.get_item(Key={"User":user})["Item"]

    #portfolio = userInfo["Availability"]
    print("Hello World")
    #if request.method == 'POST':
        #action = request.form.get('action')
        #coin = request.form.get('coin')
        #amount = request.form.get('amount')
            
        # table.put_item(Item={
        #     columns[0] : user,
        #     columns[1] : userInfo["Password"],
        #     columns[2] : userInfo["Balance"],
        #     columns[3] : userInfo["Portfolio"]
        # })
    return render_template("index.html")#, name=user, accountPortfolio=portfolio, accountBalance=balance)

@user_views.route('/')
def index():
    return render_template("index.html")