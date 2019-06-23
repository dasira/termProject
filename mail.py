# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

def Send(str):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('dasirama96@gmail.com', 'kjwoong14!')

    msg = MIMEText(str)
    msg['Subject'] = '따릉이 문의'
    msg['To'] = 'dasirama16@naver.com'
    smtp.sendmail('dasirama96@gmail.com', 'dasirama16@naver.com', msg.as_string())

    smtp.quit()