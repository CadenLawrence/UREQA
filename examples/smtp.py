import smtplib
import datetime
import sys
import scrape as scrape
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


addresses = scrape.getAddresses()
today = datetime.date.today()
SUBJECT = "Zillow Results for:  "+today.strftime('%b %d, %Y')
HTML = '<h1>The addresses below are the current addresses that were added into zillow:</h1>\n'+str(addresses)
FROM = 'CBzillow@gmail.com'
TO = 'caden.lawrence20@gmail.com'
HTML1 = MIMEText(HTML,'html')
# Prepare actual message
message = """From: %s\nSubject: %s\n\n%s
""" % (FROM, SUBJECT, str(HTML1))
try:
    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()

    mail.starttls()

    mail.login('CBzillow@gmail.com','lI1JpU363i2q')

    mail.sendmail(FROM,['cadenlawrence20@gmail.com'],message)
    mail.close()
    print('success')
except:
    print('fail')
