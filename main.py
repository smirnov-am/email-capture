from flask import Flask, render_template, request, abort
import boto3
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["POST"])
def new_lead():
    dynamodb = boto3.resource('dynamodb', region_name=Config.AWS_REGION)
    table = dynamodb.Table(Config.TABLE_NAME)

    # validate domain
    if request.host != Config.DOMAIN:
        abort(400)

    # validate email
    try:
        email = validate_email(request.form['email']).email
    except EmailNotValidError as e:
        abort(400)

    # save in dynamo
    table.put_item(
        Item={
            'email': email,
            'added_at': str(datetime.utcnow())
        }
    )
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
