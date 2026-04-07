'''
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

=============================================================
-데이터베이스 정리
psql -U 사용자명 -d 데이터베이스명 -h localhost:접속할ip주소(호스트명)
데이터베이스명=> CREATE USER 사용자명 WITH 비밀번호 '1234';
postgres=# CREATE DATABASE db이름 OWNER 소유자;
나가는방법: \q

'''