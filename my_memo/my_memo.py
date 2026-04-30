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
# get, post, push, delete, patch 방식이 있다.
================================================================
26.04.22

mgmt: Prometheus(시계열 database에 json 기록한다. ), Grafana(시각화 그래프)
node: NodeExporter 
email slack 여러가지 sns에 실시간 알람 띄울 수 있다.


[user1@mgmt ansible10_node_monitoring]$ ansible-playbook monitor_setup.yml
# 설치가 되었으면   http://node 의 ip주소:9100  을 입력해 본다
# http://172.16.8.200:9100 
# http://172.16.8.201:9100

[user1@mgmt ansible10_node_monitoring]$ ansible-galaxy  collection  install  prometheus.prometheus
# 설치후에  http://mgmt서버의 ip:9090 
# 을 입력하면 Prometheus 서버로 접속이 가능하다 
http://172.16.8.200:9090

[user1@mgmt ansible10_node_monitoring]$ ansible-playbook grafana_setup.yml
http://172.16.8.200:3000
admin
admin

grafana
대시보드 1860

Node Exporter	9100 : 각 서버의 리소스(CPU, RAM 등) 정보 추출
Prometheus	9090     : 메트릭 수집 및 데이터 조회 (웹 UI)
Grafana	3000         : 데이터 시각화 및 대시보드 (웹 UI)

서버에 들어가서

# yes 명령어를 허공(/dev/null)에 무한대로 쏘는 작업을 백그라운드(&)로 2개 실행합니다.
yes > /dev/null & yes > /dev/null &

#취소하기
 killall yes


 # Define query and alert condition : 특정조건이상이면 알림설정할때 
 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)

 Alerting
Notification configuration > Contact points

 
rocky8.10
ubuntu 24.04.3 LTS

=========================================================================================================
26.04.23

프로메테우스: 시계열 데이터를 가져오긴하지만 보기 힘들다. -> 그라파나 사용이유
PromQL: 프로메테우스로부터 어떠한 정보를 가져올 때 사용한다. 

실무에서 가장 많이 쓰는 Top 5 쿼리
① 서버가 살아있는지 확인 (생존 여부)
up{job="node"}
② CPU 사용률 (%)
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
③ 메모리 사용률 (%)
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100
④ 디스크 (Root 파티션) 사용률 (%)
100 - ((node_filesystem_avail_bytes{mountpoint="/"} * 100) / node_filesystem_size_bytes{mountpoint="/"})
⑤ 네트워크 수신 트래픽 (초당 MB)
rate(node_network_receive_bytes_total[5m]) / 1024 / 1024

# stress app 을 설치해서 테스트 해 볼수도 있다.

sudo dnf install stress -y

# 메모리 1.8 기가를 180 초 동안 지속 시키기

stress --vm 1 --vm-bytes 1.8G --vm-hang 100 --timeout 180s

 
aws를 인프라로 구성하기(테라폼,ansible)
보안 자격 증명 > 액세스 키 만들기 > CLI 
액세스 키, 비밀 액세스 키가 만들어 진다.

aws cli 설치 및 access 키 등록
 # 1. 최신 V2 설치 파일 다운로드
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# 2. 압축 해제 도구 설치 및 압축 풀기
sudo yum -y install unzip
unzip awscliv2.zip

# 3. 설치 스크립트 실행 (격리된 환경으로 깔끔하게 설치됨)
sudo ./aws/install

# 4. 정상 설치(버전 2) 확인
aws --version
# 출력 결과에 'aws-cli/2.x.x' 라고 나오면 성공!

- 인증키 등록
[user1@mgmt ansible10_node_monitoring]$ aws configure
액세스키 
비밀액세스키
ap-northeast-2
json  

Rocky Linux 에 Terraform(코드로 인프라를 구성할 수 있다) 설치

# 관리 도구 설치 저장소를 쉽게 추가하기 위해 yum-utils를 먼저 설치합니다.
sudo dnf install -y yum-utils
#HashiCorp 공식 저장소(Repo) 추가 
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
#Terraform 설치 이제 dnf 명령어로 간단히 설치할 수 있습니다.
sudo dnf -y install terraform
#설치 결과 확인
terraform -version
-> Terraform v1.14.9

플러그인에서 HashiCorp Terraform 설치: 가독성 높이기 위함

[user1@mgmt hello]$ terraform init : 테라폼 문서를 바탕으로 세팅. 자원 추가할때마다 실행
[user1@mgmt hello]$ terraform plan : 에러없이 잘실행되는지 체크
[user1@mgmt hello]$ terraform apply : 적용
[user1@mgmt hello]$ terraform destroy : 삭제

terraform으로 infra를 자동 구성하고
ansible로 infra에 있는 EC2 등의 
자원에 필요한 패키지 설치 및 bootstrapping

- 버전 주의, db는 속성값은 destory 다시만들수도있다

[user1@mgmt hello]$ terraform destroy --auto-approve: yes없이 삭제


절차적언어, 선언적언어(테라폼)

file>preferences>configure>Configure Snippets>terraform 입력>스니펫에서 가져온거 복사
스니펫: https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode

스니펫에서 가져온거 terraform.json에 복사
	"terraform 버전": {
		"prefix": "terra",
		"body": [
			"terraform {",
			"    required_version = \"~>1.14.0\"",
			"    required_providers {",
			"      aws = {",
			"            source = \"hashicorp/aws\"",
			"            version = \"~> 6.0\" ",
			"      }",
			"    }",
			"}"
		],
		"description": "terraform 버전"
	}

이후에 간편하게 사용할 수 있다. 

========================================================
26.04.24

# 라우팅 테이블 : 트레픽 이정표
resource "aws_route_table" "public_rt" {
    # 어떤 vpc 의 소속인지 설정
    vpc_id = aws_vpc.main.id
    # 라우팅 규칙 (0.0.0.0/0) 으로 가는 트레픽은 인터넷 게이트(igw) 웨이로 보내라
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw.id
    }
}


# public subnet 을 위의 라우팅 테이블로 연결
resource  "aws_route_table_association" "a" {
    subnet_id       = aws_subnet.public_subnet.id # 우리가 만든 퍼블릭 서브넷은
    route_table_id  = aws_route_table.public_rt.id # 위에서 만든 라우팅 테이블로 연결
}


# pem 파일 관련 작업


# 알고리즘 결정
resource "tls_private_key" "pk" {
    algorithm = "RSA"
    rsa_bits  = 4096
}
# 키등록
resource "aws_key_pair" "kp" {
    key_name   = "lecture-key"
    public_key = tls_private_key.pk.public_key_openssh
}


# 개인키를 가져오기
# "local_file" resource 를 이용하면 파일을 생성할수 있다.
resource "local_file" "ssh_key" {
    # ${path.module} 은 현재 실행경로를 의미한다.
    filename        = "${path.module}/lecture-key.pem"
    content         = tls_private_key.pk.private_key_pem
    file_permission = "0600" # 파일의 권한 설정
}

온프레미스 1개
인스턴스 2개 
micro nano

cloudflare에서 요청올때 클라우드환경은 대상그룹 으로  인스턴스(ec2) 로 2개 1개는 nat, 나머지는 cloudflare로 온프레미스로 향하게끔 인데 ip(온프레미스:cloudflare를 통한 전송)으로 



===================================================================
26.04.27
1. camel case :소문자,대문자
2. snake case :_
3. cabob case :-

'''