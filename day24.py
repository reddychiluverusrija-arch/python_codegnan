# import smtplib
# sender="reddychiluverusrija@gmail.com"
# password="bwfgtyzstpvyehcq"
# receiver="sreejachiluveru58@gmail.com"
# message="hi sir"
# with smtplib.SMTP('smtp.gmail.com',587) as conn:
#     conn.starttls()
#     conn.login(sender,password)
#     conn.sendmail(sender,receiver,message)
# print("email sent successfully")
import smtplib
from email.message import EmailMessage
sender="reddychiluverusrija@gmail.com"
password="bwfgtyzstpvyehcq"
receiver=["sreejachiluveru58@gmail.com","wd.rkad@gmail.com"]
msgobj=EmailMessage()
msgobj['from']=sender
msgobj['BCC']=','.join(receiver)
msgobj['subject']="SMTP mail"
msgobj.set_content("hi sir")
filename='nature.png'
with open(filename,'rb') as file:
    msgobj.add_attachment(file.read(),maintype='application',subtype='octet-stream',filename=filename)
with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.send_message(msgobj)
print('email successfully sent')