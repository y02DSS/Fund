from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib
 
 
def send_for_email(email, text1, text2, title, file=None):
    msg = MIMEMultipart()
    
    password = "qAUxc2S4cyUFydzrQHgT"
    msg['From'] = "elysium.2022@mail.ru"
    if email is not None:
        to = ["info@elysium2022.ru", "y02sofronov@yandex.ru"]
        to.append(email)
        msg['To'] = ', '.join(to)
    else:
        msg['To'] = "info@elysium2022.ru"
    msg['Subject'] = title

    if file is not None:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'%(file))
        msg.attach(part)
        
    msg.attach(MIMEText(text1))
    msg.attach(MIMEText(text2))


    server = smtplib.SMTP('smtp.mail.ru: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()

    