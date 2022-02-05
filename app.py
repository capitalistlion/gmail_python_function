import requests
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import logging
import json

# make it print to the console.
log = logging.getLogger()
console = logging.StreamHandler()
log.addHandler(console)
log.setLevel(logging.INFO)

# designing your email using HTML
def get_html_content(subject, email_content):
    html_email = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>"""+str(subject)+"""</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <!-- styles -->
        <link href="https://getbootstrap.com/2.3.2/assets/css/bootstrap.css" rel="stylesheet">
        <style>
        body {
            padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
        }
        </style>
        <link href="https://getbootstrap.com/2.3.2/assets/css/bootstrap-responsive.css" rel="stylesheet">

    </head>
    <body>
        <div class="container">

        <h1>"""+str(subject)+"""</h1>
        <p>"""+str(email_content)+"""</p>

        </div> <!-- /container -->
    </body>
    </html>
    """
    return html_email

def send_email(receiver_email, cc_emails, subject, email_content):
    html_email = get_html_content(subject, email_content)
    log.info("html content generated")
    EMAIL_FROM = "youremail@gmail.com"
    app_password = "000000000000" # you can create an app password from your gmail account security settings
    msg_html_content = MIMEText(html_email, 'html', 'utf-8')
    msg = MIMEMultipart("alternative")
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg['From'] = "TestName "+str(EMAIL_FROM) # You can replace where EMAIL_FROM is supposed to be with a custom domain if you've linked it to your mail provider and confirmed it
    msg['To'] = receiver_email
    msg['CC'] = ",".join(cc_emails)
    msg.attach(msg_html_content)
    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    # Perform operations via server
    server.login(EMAIL_FROM, app_password)
    server.sendmail(EMAIL_FROM, [receiver_email], msg.as_string())
    server.quit()
    return 'success'

response = send_email("example@gmail.com", [], "Testing Function", "Hi there. It's working well")
log.info("response - "+str(response))
