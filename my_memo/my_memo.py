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

'''