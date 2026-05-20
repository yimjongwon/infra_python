'''
====================================================
26.05.06

# DB 설치 완료후 DB를 복구하는 작업

#데이터 베이스 생성
postgresql_database:
    - name: "scott_db"
    - owener: "scott"

    # 계정 생성 및 비밀번호 
postgresql_users:
    - name: "scott"
    password: "tiger"
    - name: "postgres"
    password: "postgres"

-> db복구 테스트하기전에 yml파일에서 삭제

db복구하는 2가지 방법
test04_postgres_db_recover: 온프레미스 서버에 db백업
test04_postgres_db_recover2: s3로 db 백업

1. 서버에 db백업

# /tmp 폴더로 이동
cd  /tmp

# pg_dumpall 을 실행하기 위해 postgres 계정으로 변신해서  백업파일 생성
# 실습을 위해 수동으로 하지만 실제로는 일정주기로 자동으로 하게 해야 한다.
sudo  -u  postgres  pg_dumpall  -f  /tmp/full_db_backup.sql

# mgmt 서버에서 testvm1 에 있는 /tmp/full_db_backup.sql 파일을 현재 경로로 가져오기
scp  root@172.16.8.101:/tmp/full_db_backup.sql   .

2. s3_bucket에 db백업

# s3 버킷 및  IAM 설정
# s3 버킷 정의하기
# IAM role 정의
# 신분증에 권한 적기
# 신분증을 aws 가 인식할수 있도록  case 에 담기
# 생성된 s3 의 버킷 이름 출력

DB 백업 파일을 s3에 업로드 하는 작업
# 생성된 s3 bucket 이름
db-backup-storage-9fe4f90b

# full_db_backup.sql 파일을 s3 버킷에 동일한 파일명으로 업로드하기
aws s3 cp ./full_db_backup.sql s3://db-backup-storage-9fe4f90b/full_db_backup.sql

# 목록 확인하기
aws s3 ls s3://db-backup-storage-9fe4f90b/


- DB 복구 후에 실제 테스트
# 43.201.16.51 은 본인의 ec2 public ip 를 넣어야 한다
ssh ec2-user@43.201.16.51 -i lecture-key.pem
# 접속 확인 
psql -U scott -d scott_db -h localhost
# 비밀번호 tiger 를 입력해서 접속이 되는지 확인하고 SELECT 도 해본다.
SELECT * FROM post ;  



'''