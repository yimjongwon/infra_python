'''
- python 수업 소스코드
https://github.com/oli999/infra_python

snippet : 커맨드 설정
-https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode

cisco packet tracer
https://www.netacad.com/launch?id=ec0847b7-e6fc-4597-bc31-38ddd6b07a2f&tab=curriculum&view=b0e094c5-ca1f-59f9-9bcb-e44ea6a1dcbb

DB원격접속:Download | DBeaver Community     

ngrok:  ( 역방향 터널링 )
ngrok: AI & API Gateway | Secure Tunnels & Traffic


=============================================================================

설치 정리
pip install pyyaml
pip install jinja2

# 템플릿 파일이 위치한 폴더 설정
from jinja2 import Environment, FileSystemLoader, Template

import tkinter as tk
from tkinter import messagebox

# 현재 디렉토리의 내용확인
ls -l, ls -al

# yum 페키지 메니저를 이용해서 httpd  서버 설치
yum   install  -y  httpd

# httpd 서버 시작
systemctl  start  httpd

#재부팅 되어도 자동 시작되도록
systemctl  enable httpd 

# 웹서버가 동작하는지 확인
curl  http://localhost

# 외부 window 에서 chrome 을 실행해서  http://172.16.8.101:80 으로 접속하면 
# 방화벽(firewall) 때문에 접속이 불가하다 
# 방화벽을 내려 보자
systemctl  stop  firewalld
systemctl  disable  firewalld  # 재부팅 했을때도 내려 가도록 

import os

# yum 페키지 메니저 업데이트 (Linux 설치후 최초 한번만 하면 된다)
yum update -y
# 만일 python 이 설치 되어 있지 않으면 (rocky linux 는 이미 설치 되어 있다)
yum install -y python3 
# python 가상 환경 생성
python3  -m  venv  venv
# 가상환경 활성화
source  venv/bin/activate
# python 페키지 메니저 update
pip  install  --upgrade  pip
# 의존 페키지 설치
pip  install  fastapi  uvicorn  jinja2
# 의존 페키지  freeze
pip  freeze  >  requirements.txt
# fastapi  서버실행
uvicorn  main:app  --host  0.0.0.0  --port  8000

=============================================
nginx 설치
sudo  dnf  install  nginx -y 
# 지금 바로 시작
sudo systemctl start nginx

# 서버가 재부팅 될때 자동으로 시작 되도록 설정
sudo systemctl enable nginx

# 테스트로 실제 80 port 에서 응답하는지 확인 
curl http://localhost:80


'''