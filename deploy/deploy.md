## How to deploy on AWS

1. Create AWS account and setup access key ID and secret access key [docs](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html)
2. Install AWS CLI [docs](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. Create tables (replace region with preferred AWS region name or just leave as is)
```commandline
aws cloudformation create-stack --template-body file://./deploy/tables.yaml  --stack-name email-leads  --region us-east-1 
```
4. Make sure you have Python 3 on your laptop [docs](https://realpython.com/installing-python/)
```commandline
python3 -V
>>> Python 3.9.12
```
5. Setup python environment
```commandline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
6. Change setting in `zappa_settings.json` (lines 5 and 11-15)
- line 5 - your AWS region, replace 'us-east-1' with your region
- line 11 - your AWS region once again
- line 12 - your Google Analytics tag, replace 'G-12345' with your tag
- line 13 - your Google Analytics event you'll see in analytics
- line 14 - your DynamoDB table name, don't change
- line 15 - your domain name, replace 'example.com' with your domain
7. Deploy
```commandline
zappa deploy prod
```
You'll get your URL you'll add as HTML form action
```commandline
Your updated Zappa deployment is live!: https://123qweasdzxc.execute-api.us-east-1.amazonaws.com/prod
```
8. Create HTML form referencing the URL from previous step

```html
<form id="email-form" action="https://123qweasdzxc.execute-api.us-east-1.amazonaws.com/prod" method="POST" accept-charset="UTF-8" autocomplete="off" novalidate>
  <input class="mail" id="email" type="email" name="email" placeholder="Enter email address" autocomplete="off">
  <input class="submit-button" type="submit" value="Sign Up">
</form>
```

