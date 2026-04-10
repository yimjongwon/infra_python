'''
=================================================================
26.04.10

ansible 설치하기 mgmt에서
sudo yum -y install epel-release
sudo yum -y install ansible
[user1@mgmt ~]$ ansible --version

sudo vi /etc/ansible/hosts :인벤토리 파일

[seoul]
172.16.1.201

[jeju]
172.16.1.202

[user1@mgmt ~]$ ansible all(호스트지정) -m ping   : 모든서버에 핑
[user1@mgmt ~]$ ansible all -a "python3 --version" :버전확인
[user1@mgmt ~]$ ansible all -m file -a "path=/tmp/ansible_test.txt state=touch" -b
 :대상서버에 txt파일 만들기
[user1@rocky01 ~]$ ls /tmp :대상서버에서 파일 확인
[user1@mgmt ~]$ ansible all -m file -a "path=/tmp/ansible_test.txt state=absent" -b
 :대상서버에 txt파일 삭제

 add hoc:한번에하나, 플레이북:여러가지

[user1@mgmt ~]$ ansible all -m shell -a "free -h"
[user1@mgmt ~]$ ansible all -m shell -a "df -h"

all:어떤 inventory 그룹
-m:모듈
-b: sudo-> 없으면 user1
-i:inventory
-a:어떤 작업을 할것인지

git 삭제
[user1@mgmt ~]$ ansible all -m package -a "name=git state=absent autoremove=yes" -b

nginx 모두 설치
[user1@mgmt ~]$ ansible all -m package -a "name=nginx state=present" -b
[user1@mgmt ~]$ ansible all -m shell -a "systemctl status nginx" -b
nginx 시작하기 
[user1@mgmt ~]$ ansible all -m service -a "name=nginx state=started enabled=yes" -b
상태확인
[user1@mgmt ~]$ ansible all -m shell -a "systemctl status nginx" -b
nginx stopped
[user1@mgmt ~]$ ansible all -m service -a "name=nginx state=stopped enabled=no" -b

mgmt파일을 이동하려면 
/usr/share/nginx/html/ 로보내야한다
[user1@mgmt ~]$ ansible all -m copy -a "src=./index.html dest=/usr/share/nginx/html/index.html" -b

특정 위치로만 파일보내는법
-seoul폴더들어가서 seoul로보내기
[user1@mgmt ansible_seoul]$ ansible seoul -m copy -a "src=./index.html dest=/usr/share/nginx/html/index.html" -b
-jeju폴더들어가서 jeju로보내기
[user1@mgmt ansible_jeju]$ ansible jeju -m copy -a "src=./index.html dest=/usr/share/nginx/html/index.html" -b

인벤토리 파일의 default 참조 위치: /etc/ansible/hosts

참조위치는 원하는곳으로 설정할 수 있다
[user1@mgmt ~]$ mkdir ansible01 && cd ansible01
[user1@mgmt ansible01]$ cat <<EOF > my_host.ini(이벤트파일은 ini,lst라고 보통지정한다)
[rocky]
172.16.1.201

[rocky2]
172.16.1.202
EOF
[user1@mgmt ansible01]$ ansible rocky -i my_host.ini -m ping
[user1@mgmt ansible01]$ ansible rocky2 -i my_host.ini -m ping

인프라 프로비저닝 rocky
쿠버네티스,도커 ubuntu
우분투는 root가막혀있어서 sudo(rocky의 wheel)로해야한다

mgmt서버에 새로 추가된 ubuntu linux 들어가기
ssh로 들어갈땐 key가 필요하다 
ssh-copy-id -i ~/.ssh/ansiblekey.pem.pub user1@172.16.1.202

- mgmt 서버에서  새로 추가된  ubuntu linux 를  inventory 에 등록한다.
sudo  vi   /etc/ansible/hosts

[seoul]
172.16.1.201
172.16.1.202

[jeju]
172.16.1.203

실행전 체크
[user1@mgmt ansible03]$ ansible-playbook hello.yml --check 
yml 실행
[user1@mgmt ansible03]$ ansible-playbook hello.yml 

user1@ubuntu01:~$ htop
user1@ubuntu01:~$ cat /tmp/htop_status.txt
htop 설치 완료.
 터미널에 htop을 입력해보세요user1@ubuntu01:~$

user1@rocky02 ~]$ sudo yum update -y


'''