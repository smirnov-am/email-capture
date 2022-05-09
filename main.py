from flask import Flask, render_template, request
import boto3
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["POST"])
def new_lead():
    dynamodb = boto3.resource('dynamodb', region_name=os.getenv("AWS_REGION"))
    table = dynamodb.Table("telegr-email-leads")
    table.put_item(
        Item={'email': request.form['email'],
              'datetime': str(datetime.utcnow())
              }
    )
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
