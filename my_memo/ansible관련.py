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
================================================================
- 26.04.13

# 1. Git 패키지 설치 (root 권한으로 실행)
ansible all -m package -a "name=git state=present" -b

# 2.git user.name 설정
[user1@mgmt ~]$ ansible all -m git_config -a "name=user.name value='yim' scope=global" \
> -b --become-user user1
git user.email 설정
[user1@mgmt ~]$ ansible all -m git_config -a "name=user.email value='awosung00@naver.com' scope=global" \
> -b --become-user user1

# 3 .gitconfig 파일 확인
[user1@rocky01 ~]$ ls -al
-rw-r--r--  1 user1 user1   48 Apr 13 10:19 .gitconfig
[user1@rocky01 ~]$ cat .gitconfig
[user]
        name = yim
        email = awosung00@naver.com

#user1의 홈폴더에있는 .gitconfig 파일 제거하는법
[user1@mgmt ~]$ ansible all -m file -a "path=~user1/.gitconfig state=absent" -b

#git이 제거되었는지 확인
[user1@mgmt ~]$ ansible all -a "which git" -b
[user1@mgmt ansible03]$ vi git_install.yml 
---
- name: Git 설치 및 사용자 환경 설정
  hosts: all
  become: yes

  tasks:
    - name: 1. Git 패키지 설치
      package:
        name: git
        state: present
[user1@mgmt ansible03]$ ansible-playbook ./git_install.yml

git 제거해보기
[user1@mgmt ansible03]$ ansible-playbook ./remove_git.yml --check


git 설치 user.name, user.email 설정 추가
[user1@mgmt ansible03]$ cat install_git.yml
---
- name: Git 설치 및 사용자 환경 설정
  hosts: all
  become: yes

  tasks:
    - name: 1. Git 패키지 설치
      package:
        name: git
        state: present
    
    - name: 2. user.name 설정
      git_config:
        name: user.name
        value: "yim jongwon"
        scope: global
      become: yes
      become_user: user1 # user1으로 변신해서 작업하기
    
    - name: 3. user.email 설정
      git_config:
        name: user.email
        value: "awosung00@naver.com"
        scope: global
      become: yes
      become_user: user1

git 설정파일 제거
[user1@mgmt ansible03]$ vi remove_git.yml
---
- name: Git 제거하기
  hosts: all
  become: yes
  tasks:
    - name: 1. Git 삭제 및 미사용 의존성제거
      package:
        name: git
        state: absent
        autoremove: yes
    
    - name: 2. Git 설정파일 제거
      file:
        path: ~user1/.gitconfig
        state: absent

    - name: 3. 만일 제거할 파일이 여러개라면
      file:
        path: "{{ item }}"
        state: absent
      loop:
        - "~user1/test1.txt"
        - "~user1/test2.txt"
        - "~user1/test3.txt"

설정파일 제거 확인
[user1@mgmt ansible03]$ ansible-playbook remove_git.yml --check


my_hosts.ini파일과 ansible.cfg파일을 이용해서 default inventory를 지정할수있다.

#my_hosts.ini
[rocky]
172.16.1.201
172.16.1.202

[ubuntu]
172.16.1.203

# ansible.cfg
[defaults]
inventory = ./inventories/my_hosts.ini

register: epel_result # 작업의 결과를 epel_result 라는 변수에 담아 오겠다는 의미
var: epel_result # var 속성에 변수명만 적음, 변수만 가져올때 사용
msg: "epel_result 변수의 내용 : {{ epel_result }}\
        , 변경여부 : {{epel_result.changed}}" # msg 속성에 문자열 작성

[user1@mgmt ansible03]$ ansible-playbook var_test3.yml
---
- name: 외부 배열 변수 활용 연습
  hosts: all
  become: yes

  vars_files:
    - ./variables/my_list.yml

  tasks:
    - name: 1. 여러개의 패키지를 한번에 설치
      package:
        name: "{{ item }}"
        state: present
      loop: "{{target_packages}}"
    
    - name: 2. dict 형태의 변수를 참조해서 활용하기
      debug:
        msg: |
            번호 : {{ info.num }}
            이름 : {{ info.name }}
            주소 : {{ info.addr }}
    
    - name: 3. list 안에 dict가 들어 있는 형태의 데이터 활용하기
      debug:
        msg: |
          번호: {{ item.num }}
          이름: {{ item.name }}
          주소: {{ item.addr }}
      loop: "{{ members }}"

ansible폴더/inventories/my_hosts.ini
[rocky]                             :그룹
#호스트이름 ansible_host=아이피주소
rocky01 ansible_host=172.16.1.201   :ip주소대신 호스트이름 가져온다
rocky02 ansible_host=172.16.1.202

[ubuntu]
ubuntu01 ansible_host=172.16.1.203

ansible폴더/ansible.cfg 
[defaults]
inventory = ./inventory/my_hosts.ini 
stdout_callback = yaml                  :형식 yaml(기본 json)
# addhoc 방식으로 실행했을때도 알아 보기 쉽게(yml)
bin_ansible_callbacks = True
        
'''