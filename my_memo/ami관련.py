'''
ami를 직접 만들 수 있다.
장점?
필요한 패키지를 미리 설치해놓을수가있다.
nginx,fastapi,postgresql,ansible,terraform

EC2 ip를 미리알수없고 하나하나 설치하기 번거롭다-> 미리 준비된 AMI를 사용한다.
버전 업데이트도 가능하다.

만드는방법: packer 를 이용해서 aws에 직접 접속해서 만들면서 AMI에 등록할수있다.
https://developer.hashicorp.com/packer/install#linux



packer설치(CentOS/RHEL)
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install packer

[user1@mgmt ~]$ packer --version
Packer v1.15.3

pkr.hcl로 packer 파일만든다.

extensions에서 packer 다운로드 받으면 도움받을수있다.

# 아래의 동작이 잘 되기 위해서는 aws 설정이 되어 있어야한다. (인증키)
# ansible을 사용할꺼라면 ansible도 설치가 되어 있어야 한다. (mgmt 서버에)
# 아래의 작업은 설정만 미리 되어 있으면 github action 에서도 가능하다

이미지 굽는 방법
# packer 초기화
[user1@mgmt test07_packer]$ packer init ami_web.pkr.hcl
# packer로 ami 이미지 만들어서 aws에 등록
[user1@mgmt test07_packer]$ packer build ami_web.pkr.hcl


==========================================================
26.05.19
packer를 이용해서 ami1.0 생성 -> build -> terrafrom 실행
버전 업데이트 시
packer를 이용해서 ami1.1 생성 -> build -> terrafrom 실행

'''