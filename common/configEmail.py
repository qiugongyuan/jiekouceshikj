import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail(object):

    def send_email(self):
        msg_from = '360960443@qq.com'  # 发送方邮箱
        passwd = 'biajfsrgbswnbjje'  # 填入发送方邮箱的授权码
        msg_to = '360960443@qq.com'  # 收件人邮箱

        subject = "python邮件测试"  # 主题
        f = open("F:\\jiekouceshikj\\result\\report.html", 'rb')
        content = f.read()

        mail_mul = MIMEMultipart()  # 构建一个邮件对象
        mail_text = MIMEText("各位好，附件是本次的测试报告，请查阅!谢谢", "plain", "utf-8")  # 构建邮件正文
        mail_mul.attach(mail_text)  # 把构建好的邮件正文附加到邮件中
        # 设置附件
        msg = MIMEText(content, 'html', 'utf-8')
        msg['Content-type'] = 'application/octet-stream'
        msg['Content-disposition'] = "attachment; filename ='test.html'"
        mail_mul.attach(msg)  # 将附加按添加到邮件中

        # 邮件对象

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
