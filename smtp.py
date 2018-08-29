import smtplib

content = 'spencer is a gay little hoe'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('CBzillow@gmail.com','lI1JpU363i2q')

mail.sendmail('CBzillow@gmail.com','caden.lawrence20@gmail.com',content)
mail.close()