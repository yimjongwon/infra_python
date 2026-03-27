'''
json정리
json.load(info) str->dict
json.dump(info) dict->str
yaml정리
yaml.sage_load(info) str->dict
yaml.dump(info) dict->str

git 정리
git init
git add 파일명
git add .
git commit -m "메시지"
git commit
git switch master
git checkout master
git merge lab1
git branch
git branch -d 브랜치
git branch -D 브랜치
git log --graph --oneline --all
git restore
git restore --staged:스테이지 올라간 거 취소
git reset --soft: commit 메시지 잘못 작성했을 때, add할 파일을 누락했을때
git reset --mixed: 여러개의 파일을 만들고 작업을 했는데 그중에 일부분만 
                    잘못 작성했을때
git reset --hard HEAD~ :처음부터 다시 시작하고 싶을때
git reset --hard HEAD~~

git pull origin master= git fetch origin master + git merge origin/master

-작업하다가 임시 저장하고 다른 브랜치로 이동할때
git stash -u
가상환경 정리 
PowerShell -> Set-ExecutionPolicy RemoteSigned
python -m venv venv
.\venv\Scripts\activate

- python 수업 소스코드
https://github.com/oli999/infra_python

snippet : 커맨드 설정
-https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode

cisco packet tracer
https://www.netacad.com/launch?id=ec0847b7-e6fc-4597-bc31-38ddd6b07a2f&tab=curriculum&view=b0e094c5-ca1f-59f9-9bcb-e44ea6a1dcbb

설치 정리
pip install pyyaml
pip install jinja2

# 템플릿 파일이 위치한 폴더 설정
from jinja2 import Environment, FileSystemLoader, Template

import tkinter as tk
from tkinter import messagebox

# 현재 디렉토리의 내용확인
ls -l

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



**vm1 or ec2 로그인** 정리: ***서버*에는 .pem의 개인키, *로컬*에는 공개키의 구조**

```plaintext
[root@testvm1 /]# cat test_key.pem.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDC3h50Nki/sS4lzSFamDBNz8SRQulZkIjIZt5KOXsK6wNxn9u9n2SZY+gYBUGiugI7jU1usvSs6s90kBaeO8BQYJSQaXrj+b4Oi7YM0Fll/A9HzD6SjUOYeuQUmMNlBCHtuQpztewTOU4M9lTI873HV6NE6vXJwtUUvimVaDOUS7d+txQ6l9XDKinZlW2dszLJOEt2tR9poTH1asLZFq1IORQkskgroSYFK0NdjvE3uLuj7nt9zK94RDHKUAB55u8K3hU0Vn85ytNgSaEvj3AOgdi4jKhMsvt/dcMDnOjuYla9z+AICvx0pvt/8dcnWrKja7aIXoo+ABuJ+dnEZZyx9oYBb40iNmHtZEtIIhspbD/zRZxfQlGerIvI02QZnzu5SSWOwSbpmvc8up0a+HDbWSDpGTVvkD/MxpTqxuqkd8dWLhO4QJvOL6/nVQlhgqImWrB/aQyMHfJkkQDzKGypQr9dnsYsCyQlIMHrz+slZjnhNfu3x2vhOkC2s5aq9ac= root@testvm1
[root@testvm1 /]# cat test_key.pem.pub >> ~/.ssh/authorized_keys
[root@testvm1 ~]# chmod 600 ~/.ssh/authorized_keys:권한 낮추기
ssh-keygen -q -N "" -f test_key.pem: 공개키, 개인키 두개 생성 
-rw-------    1 root root 2602 Mar 27 15:10 test_key.pem
-rw-r--r--    1 root root  566 Mar 27 15:10 test_key.pem.pub
```
'''