'''
json정리
json.load(info) str->dict
json.dump(info) dict->str
yaml정리
yaml.sage_load(info) str->dict
yaml.dump(info) dict->str
==============================================================================
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
git stash pop 기록삭제하고 되돌리기
git stash apply 기록저장하고 되돌리기
============================================================================
가상환경 정리 
PowerShell -> Set-ExecutionPolicy RemoteSigned
python -m venv venv
.\venv\Scripts\activate
============================================================================

- python 수업 소스코드
https://github.com/oli999/infra_python

snippet : 커맨드 설정
-https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode

cisco packet tracer
https://www.netacad.com/launch?id=ec0847b7-e6fc-4597-bc31-38ddd6b07a2f&tab=curriculum&view=b0e094c5-ca1f-59f9-9bcb-e44ea6a1dcbb


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

======================================================================
[ private ec2 에  postgre DB 를 설치해 보자 ]

# 리포지토리 업데이트
sudo dnf update -y
 
# 서버 및 클라이언트 설치
sudo dnf install -y postgresql15-server

sudo postgresql-setup --initdb

sudo systemctl start postgresql
sudo systemctl enable postgresql

# 상태확인
sudo systemctl status postgresql

[ DBeaver 설치해서 postgre DB 원격접속해 보기]

 DBeaver 설치: https://dbeaver.io/download/


디폴드 옵션으로 설치한다.

[ DB 를 외부에서 접속가능하게 하기 ]

sudo vi /var/lib/pgsql/data/postgresql.conf

편집기로 위의 파일을 열어서 
listen_addresses = 'localhost' 부분을 listen_addresses = '*'로 수정 (주석 # 제거 필수!)
수정후  :wq   해서 저장하고 빠져 나온다.

접속 권한 설정 (pg_hba.conf)
sudo vi /var/lib/pgsql/data/pg_hba.conf

파일 맨 아래에 다음 줄 추가 (VPC 내부 대역 허용):
host    all             all             10.0.0.0/16            md5
서비스 재시작
sudo systemctl restart postgresql
DB 계정 비밀번호 설정
# postgres 유저로 전환
sudo -u postgres psql

# 비밀번호 변경 (홀따옴표 주의!)
ALTER USER postgres WITH PASSWORD '1234';

# 나가기
\q
[ DBeaver 를 이용해서 jump 접속하기 ]

--------------------------------------------------------------------------
[ rocky linux postgre설치 ]

# rocky linux 는 이걸 먼저 실행하고 아래를 진행한다 (공식 저장소로 업데이트)
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm

sudo dnf -qy module disable postgresql

# 저장소 추가 후 실제 패키지 설치 (서버와 클라이언트) 
sudo dnf install -y postgresql15-server postgresql15

# 1. DB 초기화
sudo /usr/pgsql-15/bin/postgresql-15-setup initdb

# 2. 서비스 시작 및 자동 실행 설정
sudo systemctl enable postgresql-15 
sudo systemctl start postgresql-15

# 3.  postgres 로 user 전환
su  -   postgres

# 4. psql 실행
psql

# 비밀 번호 변경
ALTER USER postgres WITH PASSWORD '1234';
\q

# root 계정으로 다시 전환 (비밀번호는 test123)
su  -  root  # 또는 exit

# 모든 ip 에서 접속 할수 있도록
sudo vi /var/lib/pgsql/15/data/postgresql.conf

#listen_addresses = 'localhost'  를 변경  listen_addresses = '*'

# 접속 권한 설정
sudo vi /var/lib/pgsql/15/data/pg_hba.conf

#맨 아래에 추가 
host   all   all   0.0.0.0/0   md5

# 서비스 재시작
sudo systemctl restart postgresql-15

# user 전환 
su  -  postgres

# 테스트로 접속해 보기  
psql  -U postgres  -d  postgres


==================================================
인프라 삭제 권장 순서

- 가장 안쪽의 '비싼' 자원부터 밖으로 나오면서 지우기

Ec2 => NAT => subnet =>  internet gateway => vpc 
==================================================


====================================================================================

**vm1 or ec2 로그인** 정리: ***서버*에는 .pem의 개인키, *로컬*에는 공개키의 구조**

```plaintext
[root@testvm1 /]# cat test_key.pem.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDC3h50Nki/sS4lzSFamDBNz8SRQulZkIjIZt5KOXsK6wNxn9u9n2SZY+gYBUGiugI7jU1usvSs6s90kBaeO8BQYJSQaXrj+b4Oi7YM0Fll/A9HzD6SjUOYeuQUmMNlBCHtuQpztewTOU4M9lTI873HV6NE6vXJwtUUvimVaDOUS7d+txQ6l9XDKinZlW2dszLJOEt2tR9poTH1asLZFq1IORQkskgroSYFK0NdjvE3uLuj7nt9zK94RDHKUAB55u8K3hU0Vn85ytNgSaEvj3AOgdi4jKhMsvt/dcMDnOjuYla9z+AICvx0pvt/8dcnWrKja7aIXoo+ABuJ+dnEZZyx9oYBb40iNmHtZEtIIhspbD/zRZxfQlGerIvI02QZnzu5SSWOwSbpmvc8up0a+HDbWSDpGTVvkD/MxpTqxuqkd8dWLhO4QJvOL6/nVQlhgqImWrB/aQyMHfJkkQDzKGypQr9dnsYsCyQlIMHrz+slZjnhNfu3x2vhOkC2s5aq9ac= root@testvm1
[root@testvm1 /]# cat test_key.pem.pub >> ~/.ssh/authorized_keys
[root@testvm1 ~]# chmod 600 ~/.ssh/authorized_keys:권한 낮추기
ssh-keygen -q -N "" -f test_key.pem: 공개키, 개인키 두개 생성 
-rw-------    1 root root 2602 Mar 27 15:10 test_key.pem
-rw-r--r--    1 root root  566 Mar 27 15:10 test_key.pem.pub
chmod  700  ~/.ssh
chmod  600  ~/.ssh/authorized_keys
```
=================================================================================

[ testvm1 에서 testvm2 로 접속해서 작업하기 ]

# 비밀번호를 이용해서 접속 
# ssh 계정@ip 주소
ssh  root@172.16.8.102

# pem 파일을 이용해서 접속
# ssh  -i  pem파일의위치   계정@ip주소
ssh  -i   .~/xxx.pem   root@172.16.8.102

# scp 를 이용해서 파일 전송 (비밀번호 입력 필요)
# scp   대상파일   계정@ip : 경로 

scp  ./memo.txt   root@172.16.8.102:~/ 
scp  ./memo.txt   root@testvm2:~/ 


# scp 를 이용해서 파일 전송 (pem 파일 이용)
# scp  -i  pem파일의위치   대상파일   계정@ip : 경로 

scp  -i   .~/xxx.pem   ./memo.txt   root@172.16.8.102:~/ 
scp   -i   .~/xxx.pem  ./memo.txt   root@testvm2:~/ 

==============================================================================
호스트명 정리
cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

 vi /etc/hosts
[root@testvm1 ~]# cat /etc/hosts
127.0.0.1   localhost testvm1
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
172.16.8.102 testvm2

[root@testvm1 ~]# exec bash

======================================================================================

-데이터베이스 정리
psql -U 사용자명 -d 데이터베이스명 -h localhost:접속할ip주소(호스트명)
데이터베이스명=> CREATE USER 사용자명 WITH 비밀번호 '1234';
postgres=# CREATE DATABASE db이름 OWNER 소유자;
나가는방법: \q
======================================================================================
'''