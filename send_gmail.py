import smtplib, ssl
from email.mime.text import MIMEText
import gmail_account as gmail   #계정정보 gmail_account: 지메일 계정 정보 작성한 파일명

#이메일 데이터 작성
def send_test_email():
    msg = make_mime_text(
        mail_to=gmail.account,
        mail_from=gmail.emailFrom,
        subject="제목이예요",
        body="안녕? 이메일 테스트 중이야"
    )
    send_gmail(msg)

#이메일 제목, 발신, 수신
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject    #메일 제목
    msg["To"] = mail_to         #받는 사람
    msg["From"] = gmail.account #보내는 사람
    return msg

#전송
def send_gmail(msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    #서버에 접속시 기본적으로 작성되어야 하는 코드
    server.ehlo
    server.starttls()
    server.ehlo
    server.set_debuglevel(0)    #로그 넣어줘야함
    server.login(gmail.account, gmail.password)
    server.send_message(msg)
#--------------

if __name__=='__main__':
    send_test_email()
    print("ok")