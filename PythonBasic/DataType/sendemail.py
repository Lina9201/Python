# *-* coding:utf-8 *-*

import smtplib
from email.mime.text import MIMEText

# 准备发件相关的参数
smtpserver = "smtp.163.com"
sender = "18994205919@163.com"
# 此处密码是客户端授权密码，需要在163邮箱客户端中进行设置的
psw = "zxf779616131"
receiver = "779616131@qq.com"

# 编辑邮件的内容
subject = "This is the 163 email used to send."
body = '<p>163 send emails</p>'
msg = MIMEText(body, "html", "utf-8")
msg['from'] = sender
msg['to'] = "779616131@qq.com"
msg['subject'] = subject

# 发送邮件
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.set_debuglevel(1)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("Send email successfully!")
except smtplib.SMTPException:
    print("Fail to send email!")

