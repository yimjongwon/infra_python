'''
26.05.07

tailscale

- Local Vmware
# 1. Tailscale 저장소 추가 및 설치
sudo dnf config-manager --add-repo https://pkgs.tailscale.com/stable/rhel/9/tailscale.repo
sudo dnf install tailscale -y

# 2. Tailscale 서비스 활성화 및 시작
sudo systemctl enable --now tailscaled

# 3. 로그인 및 연결
# 화면에 나오는 URL을 웹브라우저로 열어서 인증
sudo tailscale up

# 다른 node의 패킷을 받아서 외부(talescale, aws)로 전달할 수 있게 설정
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# vmware가 속한 vpc 172.16.8.0/24 대역을 aws에서도 접속하게 하기
sudo tailscale up --advertise-routes=172.16.8.0/24 --accept-routes 

- AWS EC2 설정 (Amazon Linux 2023 또는 Ubuntu 기준)

# 1. Tailscale 설치 스크립트 실행
curl -fsSL https://tailscale.com/install.sh | sh

# 2. Tailscale 서비스 시작 및 로그인
# 실행 후 화면에 나타나는 URL을 브라우저에 복사해서 인증(로그인)하세요.
sudo tailscale up

# 다른 node의 패킷을 받아서 외부(talescale, onpremise)로 전달할 수 있게 설정 
echo 'net.ipv4.ip_forward = 1' | sudo tee -a /etc/sysctl.conf 
echo 'net.ipv6.conf.all.forwarding = 1' | sudo tee -a /etc/sysctl.conf 
sudo sysctl -p 

# ec2 가 속한 vpc 10.0.0.0/16 대역을  vmware(onpremise) 에서도 접속 가능하게 광고하기
sudo tailscale up --advertise-routes=10.0.0.0/16 --accept-routes 

# 광고를 리셋하고 싶으면 아래를 입력하고 다시  광고 하면 된다.(선택사항)
sudo tailscale up --accept-routes --reset

# vpc 에 추가로 ec2 를 배치하고  onpremise 에 ping 이 가능하도록 설정(라우팅 편집)
1. onpremise의 네트워크 대역을 입력
2. 인스턴스
3. tailscale 설치 및 연결된 ec2를 선택한다.
4. 소스 /대상 확인 변경 (중지)

# 다른 모든 vmware 의 node 들에 해야할 설정
sudo ip route add 10.0.0.0/16 via 172.16.8.200

# 위의 설정을 하면 다른 node 에서도 aws 의 사설 아이피에 접근이 가능하게 된다.


=========================================================================
26.05.08

머신에 등록하고 로그인하는 과정을
자동화를 위해선 auth key가 필요

광고된 내용을 승인하는 과정을
자동화를 위해선 access key가 필요하다

ec2의 다른 서버가 대장서버를 통해 온프레미스로 전달하기위해선
source_dest_check = false
해줘야 한다

python3.12 -m pip install jmespath

# ec2가 provision 될때 실행할 script 를 지정할 수 있다.
user_data = <<-EOF
    #!/bin/bash

    #host 이름 변경
    hostnamectl set-hostname ${var.host_name}

    # /etc/hosts 에도 일관성 있게 반영
    echo "127.0.0.1 ${var.host_name}" >> /etc/hosts
EOF

# host 명으로 사용할 변수를 선언하고 기본값 전달
variable "host_name" {
    type = string
    default = "db-server"
}

=======================================================
26.05.13
- NAT Gateway
# 온프레미스에서 ec2로 ping
[user1@mgmt test05_tailscale2]$ ping -c 3 10.0.2.122
# private 서브넷에있는 ec2로 ping
[user1@mgmt test05_tailscale2]$ ping db-server -c 5
# ec2에 접속
[user1@mgmt test05_tailscale2]$ ssh ec2-user@10.0.2.122 -i lecture-key.pem
# 외부로 나가는지 확인(nat gateway->rt->igw)
[ec2-user@db-server ~]$ ping 8.8.8.8 -c 3

- NAT Instance
# 온프레미스에서 ec2로 ping
[user1@mgmt test05_tailscale3]$ ping -c 3 10.0.2.192
# ec2에 접속
[user1@mgmt test05_tailscale3]$ ssh ec2-user@10.0.2.192 -i lecture-key.pem
# ec2에서 온프레미스로 ping
[ec2-user@db-server ~]$ ping mgmt -c 5

# version 명시
# tailscale api 키와 tailnet_name 등록
# tailscale auth 키 생성
# provider 설정
# VPC 및 네트워크 생성
# 인터넷 게이트웨이
# 가용 영역 데이터 가져오기
# Public Subnet (NAT Instance가 위치할 곳)
# Public 라우팅 테이블
# public subnet 을 public_rt 로 연결
# NAT Instance용 보안 그룹
# NAT Instance(user_data로 NAT 세팅), # 부팅 시 NAT 설정 (masquerade 및 routing)
# Private Subnet 구성 (EC2가 위치할 곳)
# Private 라우팅 테이블
# Tailscale 온프레미스 연동 라우팅 (Public & Private 모두 적용)
# Public Subnet에서 172.16.8.0/24로 갈 때 대장 EC2를 거치도록 설정 (my_ec2 는 아래에 정의할 예정)
# aws_route 는 미리 만들어 놓은 aws_route_table 에 라우팅 정보를 추가하는 용도로 사용할 수 있다.
# Private Subnet에서 172.16.8.0/24로 갈 때 대장 EC2를 거치도록 설정
# 보안 및 키 설정
# 테라폼이 기기를 찾고 라우팅을 승인
# vpc로 가는길 뚫어주기




'''