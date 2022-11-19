import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='19i304@psgtech.ac.in',
    to_emails='20i464@psgtech.ac.in',
    subject='Expense Limit Reminder',
        html_content='<strong>Dear User, You have exceeded your specified monthl expense limit</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))