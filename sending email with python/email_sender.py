import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Harsh Sharma'
email['to'] = 'harsh112200sharma@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content('I am a python developer!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('iamharshsharma12@gmail.com', 'Ashokk@1')
    smtp.send_message(email)
    print('all good boss!')
