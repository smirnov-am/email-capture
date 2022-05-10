from flask import Flask, render_template, request
import boto3
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["POST"])
def new_lead():
    dynamodb = boto3.resource('dynamodb', region_name=Config.AWS_REGION)
    table = dynamodb.Table(Config.TABLE_NAME)

    table.put_item(
        Item={
            'email': request.form['email'],
            'added_at': str(datetime.utcnow())
        }
    )
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
