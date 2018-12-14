import smtplib
from email.mime.text import MIMEText

mailserver = "smtp.163.com"
username_send = '18994205919@163.com'
password = 'zxf920128'
username_recv = 'zhuxuefei@trendytech.com.cn'
mail = MIMEText('这是发用的邮件内容')
mail['Subject'] = '这是邮件主题'
mail['From'] = username_send
mail['To'] = username_recv
smtp = smtplib.SMTP(mailserver, port=25)
smtp.login(username_send, password)
smtp.sendmail(username_send, username_recv, mail.as_string())
smtp.quit()
print('success')