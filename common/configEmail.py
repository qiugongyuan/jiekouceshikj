import smtplib
from email.mime.text import MIMEText


class SendEmail(object):

    def send_email(self):
        msg_from = '360960443@qq.com'  # 发送方邮箱
        passwd = 'biajfsrgbswnbjje'  # 填入发送方邮箱的授权码
        msg_to = '360960443@qq.com'  # 收件人邮箱

        subject = "python邮件测试"  # 主题
        content = "这是我使用python smtplib及email模块发送的邮件"
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")
        except s.SMTPException as e:
            print("发送失败")
        finally:
            s.quit()


if __name__ == '__main__':
    SendEmail().send_email()
