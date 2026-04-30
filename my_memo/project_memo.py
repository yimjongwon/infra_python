'''
도메인사서
 리버스 프록시
 도메인을 네임을 연결
 로드밸랜서에서 요청을 받아서 vmware로 
 cloudflare  vmware로 트래픽을 들어오게할수있다. 
 ngrok의 상위버전이다. 
 도메인을사서 vmware를 고정할수있다
 aws에서 들어오는 트래픽을 vmware로 전달할 수 있다. 

 15.164.19.8 
 port
 22
 80
 443
 5432

 ec2_yim

 #!/bin/bash
sudosu
apt-getupdate–y
apt-getinstallnginx-y
cd/var/www/html
rmindex*
apt-getinstallnet-tools-y
ifconfiggrepinet>> index.html


#!/bin/bash
# sudo su 대신 스크립트 자체가 root 권한으로 실행되므로 sudo를 붙이거나 생략해도 됩니다.
dnf update -y
dnf install nginx -y
dnf install net-tools -y

# Nginx 서비스 시작 및 부팅 시 자동 실행 설정 (Amazon Linux는 수동 시작 필요)
systemctl start nginx
systemctl enable nginx

cd /var/www/html
rm -f index*

# 현재 인스턴스의 IP 정보를 index.html에 기록
ifconfig | grep inet | head -n 1 >> index.html

lookup('env', ~~무언가~~)


추적삭제
git update-index --assume-unchanged main.yml
git update-index --assume-unchanged postgresql_setup.yml
git update-index --assume-unchanged .gitignore


추적복구
git update-index --no-assume-unchanged [파일명]


베스천서버
sub->main
git reset --mixed HEAD~3



'''