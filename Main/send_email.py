from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib
 
 
def send_for_email(email, text, title, file=None):
    msg = MIMEMultipart()
    
    password = "qetGLzNTmCd49kpukyxz"
    msg['From'] = "sbz35@mail.ru"
    msg['To'] = "za02za02@bk.ru"
    msg['Subject'] = title

    msg.attach(MIMEText(email, text))

    if file is not None:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'%(file))
        msg.attach(part)

    server = smtplib.SMTP('smtp.mail.ru: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.send_message(msg)
    server.quit()

    