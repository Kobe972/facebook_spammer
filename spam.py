import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse

parser = argparse.ArgumentParser(description='Facebook spammer')
parser.add_argument('from_email', help='your email', type=str)
parser.add_argument('to_email', help='target email', type=str)
parser.add_argument('password', help='password', type=str)
args = parser.parse_args()

def send_email(from_addr, to_addr, subject, message):
    # 设置SMTP服务器和端口
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587  # 或者使用465（SSL）

    # 邮箱登录凭据
    username = from_addr
    password = args.password

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(message, 'plain'))

    try:
        # 连接SMTP服务器并登录
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用TLS加密
        server.login(username, password)

        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        # 关闭SMTP连接
        server.quit()

if __name__ == "__main__":
    # 读取content.txt文件内容
    with open('content.txt', 'r') as file:
        content = file.read()

    # 设置发件人、收件人及邮件主题
    from_addr = args.from_email
    to_addr = args.to_email
    subject = "Request for Reactivating FB Account"

    # 调用函数发送邮件
    send_email(from_addr, to_addr, subject, content)