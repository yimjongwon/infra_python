'''
json정리
json.load(info) str->dict
json.dump(info) dict->str
yaml정리
yaml.sage_load(info) str->dict
yaml.dump(info) dict->str

==============================================================================

user가 root 권한을 얻으려고 할때는 wheel그룹 추가하기
root 계정으로 들어간 후
usermod -aG wheel user1
[user1@testvm2 ~]$ groups
user1 wheel

user는 sudo로 관련 작업을해야한다->비밀번호물어본다->물어보지않도록 설정한다.
sudo cat /etc/sudoers에 한줄 추가하기

user1(유저이름) ALL=(ALL)   NOPASSWD: ALL
->하고 readonly여서 :wq!하기 

설정 잘되었는지 테스트하기
sudo yum install httpd -y

===================================================================================
- sed "s/이전내용/치환할내용/" 파일명 # 결과만 출력

- sed -i "s/이전/치환/" 파일명 # 실제로 바꿈
=========================================================

http:172.16.8.101:80입력했을때 리버스 프록시 port 80->8000

vm1에서 
nginx 설치
sudo  dnf  install  nginx -y 
# 지금 바로 시작
sudo systemctl start nginx

# 서버가 재부팅 될때 자동으로 시작 되도록 설정
sudo systemctl enable nginx

# 테스트로 실제 80 port 에서 응답하는지 확인 
curl http://localhost:80

cd /etc/nginx
vi nginx.conf

/etc/nginx/conf

    #붙이기->#root         /usr/share/nginx/html;

        location / {
           # 8000 번 port 에서 실행중인 서비스로 요청 전달
           proxy_pass http://localhost:8000;
           # 필수 헤더 설정
           proxy_set_header HOST $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Photo $scheme;
        }


sudo nginx -t
설정완료후
sudo systemctl reload nginx

-로드밸런싱 설정 버전
 # 서버 클러스터 그룹 설정 (로드 밸런싱 대상)
    upstream fastapi_cluster {
        # 기본값 Round Robin (요청을 돌아가면서 분배)
        # least_conn; # 현재 요청수가 가장 적은 쪽으로 요청을 보냄
        # ip_hash; # 클라이언트의 ip 를 해싱하여 항상 동일한 곳으로 보냄(session 유지)

        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
        server 127.0.0.1:8002;
    }


    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        #root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            # 8000 번 port 에서 실행중인 서비스로 요청 전달
            # proxy_pass http://localhost:8000;
            
            # fastapi_cluster 로 요청 전달
            proxy_pass http://fastapi_cluster;
            
            # 필수 헤더 설정
            proxy_set_header HOST $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Photo $scheme;
        }


        uvicorn  main:app  --host  0.0.0.0  --port  8000

========================================================--------------
26.04.09

정해진시간마다 작업해야할때 cron 사용
cron:https://crontab.guru/

        
# 주기적으로 실행할 내용 작성 crontab
[root@testvm1 script01]# crontab -e
* * * * * echo "hello crontab" >> /root/script01/crontab.log

목록확인: [root@testvm1 script01]# crontab -l
실시간확인:[root@testvm1 script01]# tail -f crontab.log
[root@testvm1 script01]# tail -n 3 crontab.log

[root@testvm1 script01]# curl -s http://localhost:8000/health || echo "fastapi is dead"
fastapi is dead
-s: 에러메시지없이 간단히 출력

postgre 백업
[root@testvm1 script01]# pg_dump "postgresql://scott:tiger@localhost:5432/scott_db" > pg_backup2.sql
매일 새벽 3시에 백업
0 3 * * * pg_dump "postgresql://scott:tiger@localhost:5432/scott_db" > /root/script01/pg_ba
ckup.sql

vi 에디터 안에서 모든 내용 삭제 하기

명령모드-> gg -> dG


표형태의 데이터중에 선택해서 가져오기
[root@testvm1 script01]# ls -l | awk '{ print $1, $3, $9 }' | tail -n 5 >> ccc.txt

날짜포맷 -> 2026-04-09 11:43:38
date +"%Y-%m-%d %H:%M:%S"
touch "report_$(date +%Y-%m-%d).txt"

무작위 출력: RANDOM
for item in "${fortune[$((RANDOM%5))]}"; do
    echo $item
done

=================================================================



'''