'''
===================================================================================

인프라 삭제 권장 순서

- 가장 안쪽의 '비싼' 자원부터 밖으로 나오면서 지우기

Ec2 => NAT => subnet =>  internet gateway => vpc 


====================================================================================


**vm1 or ec2 로그인** 정리: 서버에는 공개키(.pem.pub), 로컬(.pem)에는 개인키의 구조 -> 비밀번호 없이 접근 가능, 접근권한 600으로 맞출것(낮추기)

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

====================================================================================

[ testvm1 에서 testvm2 로 접속해서 작업하기 ]

# 비밀번호를 이용해서 접속 
# ssh 계정@ip 주소
ssh  root@172.16.8.102

# pem 파일을 이용해서 접속
# ssh  -i  pem파일의위치   계정@ip주소
ssh  -i   .~/xxx.pem   root@172.16.8.102

# scp 를 이용해서 원격지에 파일 전송 (비밀번호 입력 필요)
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
================================================================================
mgmt, rocky01, rocky02을 활용한 Ansible 환경 구성(26.04_09)

mgmt: 관리용서버, 개인키(ansiblekey.pem)
rocky01: 공개키(ansiblekey.pem.pub)
rocky02: 공개키(ansiblekey.pem.pub)

호스트네임 rocky01에서 rocky02로 변경
[user1@rocky01 ~]$ sudo hostnamectl set-hostname rocky02
                    sudo hostname rocky02

[user1@mgmt ~]$ ssh-keygen -q -N "" -f ~/.ssh/ansiblekey.pem
-q	Quiet
-N ""  비밀번호 빈값설정
-f 파일경로

rocky01에 pub전달
[user1@mgmt ~]$ ssh-copy-id -i ~/.ssh/ansiblekey.pem.pub user1@172.16.1.201
rocky02에 pub전달
[user1@mgmt ~]$ ssh-copy-id -i ~/.ssh/ansiblekey.pem.pub user1@172.16.1.202

[user1@rocky01 ~]$ ls -al ~/.ssh/
total 4
drwx------  2 user1 user1  29 Apr  9 17:16 .
drwx------. 6 user1 user1 154 Apr  9 17:16 ..
-rw-------  1 user1 user1 564 Apr  9 17:16 authorized_keys
[user1@rocky02 ~]$ ls ~/.ssh/ -al
total 4
drwx------  2 user1 user1  29 Apr  9 17:22 .
drwx------. 6 user1 user1 175 Apr  9 17:22 ..
-rw-------  1 user1 user1 564 Apr  9 17:22 authorized_keys

[user1@mgmt ~]$ cat <<EOF > ~/.ssh/config
> HOST *
>   User user1
>   IdentityFile ~/.ssh/ansiblekey.pem
>   StrictHostKeyChecking no   :접속할때 accept 안물어보는 설정
> EOF

config 폴더 권한 낮추기
[user1@mgmt ~]$ chmod 600 ~/.ssh/config

-ssh로 접속해서 hostname 물어보는 명령어
[user1@mgmt ~]$ ssh 172.16.1.201 hostname
rocky01    -> 설정 되었으면 비밀번호 안물어보고 나와야한다
[user1@mgmt ~]$ ssh 172.16.1.202 hostname
rocky02    -> 설정 되었으면 비밀번호 안물어보고 나와야한다

============================================================
인프라 프로비저닝 rocky
쿠버네티스,도커 ubuntu
우분투는 root가막혀있어서 sudo로해야한다
'''