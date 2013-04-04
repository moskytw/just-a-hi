#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

default_from = 'system@localhost.lo'
smtp_server = smtplib.SMTP('localhost')

def send(to, subject, body, from_=None):

    global default_from
    global smtp_server

    msg = MIMEText(body, _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = from_ or default_from
    if isinstance(to, basestring):
        msg['To'] = to
    else:
        msg['To'] = to =  ', '.join(to)

    return_val = smtp_server.sendmail(from_, to, msg.as_string())
    return return_val

if __name__ == '__main__':
    smtp_server.set_debuglevel(1)
    from time import sleep
    for i in range(10):
        print 'return:', send('mosky.tw@gmail.com', 'Testing No. %d' % i, 'Hi.')
        sleep(1)
