#[이메일 자동화]
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import send_gmail   #gmail 발송 모듈
import gmail_account as gmail # 계정 정보

# 메일 데이터 작성
msg = MIMEMultipart()
msg['Subject'] = '첨부파일은 스타벅스 사진입니다!'
msg['From'] = gmail.account
msg['To'] = "banishee@naver.com"
msg['Cc'] = gmail.account
msg.add_header('reply-to', 'novsunny910@gmail.com') # --- (1a)

# 본문 텍스트 작성
txt = MIMEText('오늘 구글에서 찾은 사진이예요!\n첨부 이미지를 확인해주세요.')
msg.attach(txt)

# 이미지 첨부
with open('/Users/seonheelee/autoDown/1.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)

# 메일 발송 
send_gmail.send_gmail(msg)
print("ok")