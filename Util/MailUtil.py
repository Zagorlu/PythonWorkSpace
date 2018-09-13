#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018 Taha Emre Demirkol

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import os
import smtplib
import random
import email.encoders as Encoders
from Util.PackageUtil import PackageUtil as packageControl
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailUtil:
    """
    THIS IS NOT DESCRIPTION FOR "CommandUtil.py" CLASS.
    This part represent to Static Initiliazer Code on Java, it's check to version for the avaiable version.
    At least current Python version must be 3.6.4+, anything else you should update Python version
    """
    ####################################################################################################################
    if not packageControl.checkVersionForApplicable(3, 6, 4):
        raise EnvironmentError("At least current must be 3.6.4+, anything else you should update Python version !!!")

    if packageControl.getPlatformInfo() != 'Linux' and packageControl.getPlatformInfo() != 'OS X':
        raise SystemError("This class only execute Linux or Posix OS platform !!!")
    ####################################################################################################################

    def __init__(self):
        """
        INFO: Default Constructure cannot be Creatable
        WARNING: If attand to create this object, it will raise NotImplementedError
        """
        assert NotImplementedError("This object useing only library, cannot be creatable!!!")

    def __new__(cls):
        """
        INFO: This method was overrided only avoided to __new__ operator
        :return: NOISE_OBJECT
        """
        return object.__new__(cls)

    @staticmethod
    def sendMail(mailFrom, mailTo, mailCc, mailSbj, mailBodyArray, smtpIp, attachs=[]):
        """
        This Function send e-mail with directly
        :raise If any Exception will re-raise this Exception
        :param mailFrom: Mail From part
        :param mailTo: Mail To part
        :param mailCc: Mail Cc part
        :param mailSbj: Mail Subject
        :param mailBodyArray: Mail Body Array, this part should be contain yours html body as list
        :param smtpIp: Mail STMP server IP
        :param attachs: If you have to attach objects, you can naming with array(JPG,TXT,PDF...)
        :return: NONE
        """
        try:
            mail_Text = ""
            eMailFile = "emailFile_" + str(random.randrange(1000, 9999)) + ".html"
            mailBodyFile = open(eMailFile, 'w')
            mailBodyFile.write("<html><head></head><body><p><pre>")
            mail_Text += "<html><head></head><body><p><pre>"
            for body_Line in mailBodyArray:
                mailBodyFile.write(body_Line)
                mail_Text += body_Line
            mailBodyFile.write("</pre></p></body></html>")
            mail_Text += "</pre></p></body></html>"
            mailBodyFile.close()

            mail_TO = mailTo.split(',')
            mail_CC = mailCc.split(',')

            msg = MIMEMultipart('alternative')
            msg['Subject'] = mailSbj
            msg['From'] = mailFrom
            msg['To'] = ', '.join(mail_TO)
            msg['Cc'] = ', '.join(mail_CC)

            path = os.path.dirname(os.path.realpath(__file__))
            dirs = os.listdir(path)
            for name in attachs:
                for file in dirs:
                    if name in file:
                        part = MIMEBase('application', "octet-stream")
                        part.set_payload(open(str(file), "rb").read())
                        Encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename=' + str(file))
                        msg.attach(part)

            part1 = MIMEText(mail_Text, 'plain')
            part2 = MIMEText(mail_Text, 'html')
            msg.attach(part1)
            msg.attach(part2)

            aggregatesMail = mail_TO + mail_CC
            s = smtplib.SMTP(smtpIp)
            s.sendmail(mailFrom, aggregatesMail, msg.as_string())
            s.quit()
        except Exception as e:
            raise RuntimeError("Unexpected Error : " + str(e))
