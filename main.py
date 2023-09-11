
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 

from_email = 'sender@gmail.com'
to_email = 'reciever@gmail.com'
subject = 'Subject'

message = MIMEMultipart()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject




# message to be sent
html_content = """ 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
</html>

"""

# Attach HTML content to the message
message.attach(MIMEText(html_content, 'html'))
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create an SMTP session
server = smtplib.SMTP(smtp_server, smtp_port)

# Start TLS encryption for security
server.starttls()

# Login to your Gmail account
server.login(from_email, 'password')
server.sendmail(from_email, to_email, message.as_string())
    
# except e:
#     print(e)



# terminating the session
server.quit()