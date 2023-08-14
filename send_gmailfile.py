#[이메일 자동화]
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import send_gmail   #gmail 발송 모듈
import gmail_account as gmail # 계정 정보

# 메일 데이터 작성
msg = MIMEMultipart()
msg['Subject'] = '이메일_제목_입력'  #이메일 제목
msg['From'] = gmail.account #gmail.py > account에 등록한 메일 계정으로 발신 
msg['To'] = "banishee@naver.com"    #수신용 이메일
msg['Cc'] = gmail.account
msg.add_header('reply-to', '답변용_이메일_주소_입력') #답변용 이메일

# 본문 텍스트 작성
txt = MIMEText('오늘 구글에서 찾은 사진이예요!\n첨부 이미지를 확인해주세요.')
msg.attach(txt)

# 이미지 첨부
with open('/Users/{경로경로}/1.jpg', 'rb') as fp:   #첨부할 파일
    img = MIMEImage(fp.read())
    msg.attach(img)

# 메일 발송 
send_gmail.send_gmail(msg)
print("ok")