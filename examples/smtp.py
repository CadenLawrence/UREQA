import smtplib
import datetime
import sys
import scrape as scrape
from jinja2 import Environment, BaseLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
newaddresses = []
addresses = scrape.getAddresses()
for address in addresses:
    newaddresses.append(address)
newaddresses = newaddresses
today = datetime.date.today()
SUBJECT = "Zillow Results for:  "+today.strftime('%b %d, %Y')
HTML = """
{% if addresses %}
<h3>The addresses below are the current addresses that were added into zillow:</h3>
{% for address in addresses %}
    <li><a href="https://www.zillow.com/homes/for_sale/{{address}}/">{{ address }}</a></li>
{% endfor %}
{% else %}
<h3>There are no new houses inside of the zillow database, I will check again tomorrow at 8pm.</h3>
{% endif %}
"""
FROM = 'CBzillow@gmail.com'
TO = ['caden.lawrence20@gmail.com']


# your template as a string variable
# jinja2 rendering
template = Environment(loader=BaseLoader).from_string(HTML)
template_vars = {"addresses": newaddresses ,}
html_out = template.render(template_vars)
# Prepare actual message
message = EmailMessage()
message['subject'] = SUBJECT
message['to'] = ", ".join(TO)
message['from'] = FROM
message.set_content(html_out,subtype='html')
try:
    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()

    mail.starttls()

    mail.login('CBzillow@gmail.com','lI1JpU363i2q')

    mail.send_message(message,FROM,TO)
    mail.close()
    print('success')
except Exception as e: print(e)
