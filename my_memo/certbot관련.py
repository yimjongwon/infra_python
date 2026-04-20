'''
========================================================
26.04.17
https는 80, 443 포트 열려 있어야 한다.

1. nginx서버 실행 
[user1@mgmt ansible09_nginx]$ ansible-playbook nginx_setup.yml 

2. 인증서 발급
[user1@mgmt ansible09_nginx]$ ansible-playbook certbot_setup.yml
서버들어가서 
[user1@mgmt ansible09_nginx]$ ssh user1@15.164.225.9
인증서 확인할 수 있는 곳
creates: /etc/letsencrypt/live/cloudyim.store/fullchain.pem/fullchain.pem
cat으로 fullchain.pem 확인
[user1@ip-172-31-32-227 ~]$ sudo cat /etc/letsencrypt/live/cloudyim.store/fullchain.pem


3. https 서버 실행
[user1@mgmt ansible09_nginx]$ ansible-playbook nginx_https.yml

4. 확인

- Google ai studio
Continue - open-source AI code agent

role 이용한 인증서 발급
[user1@mgmt ansible09_nginx]$ ansible-galaxy install geerlingguy.certbot


ubuntu 환경에서 https 실행해보기!!!

1. EC2 인스턴스 초기 세팅
[user1@mgmt ansible09_nginx]$ ansible-playbook ec2_bootstrap.yml --private-key ./tmp_key.pem 
2. nginx 기본 웹서버 설치 
[user1@mgmt ansible09_nginx]$ ansible-playbook nginx_setup.yml 
3. 인증서 실행전 가비아에서 dns 설정 바꾸기
- Let's Encrypt (Certbot) SSL 인증서 자동 발급 및 갱신 세팅
[user1@mgmt ansible09_nginx]$ ansible-playbook certbot_setup_ubuntu.yml 
4. https 보안 설정
[user1@mgmt ansible09_nginx]$ ansible-playbook nginx_https.yml 
5. https://cloudyim.store 접속해보기

'''