'''
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
=====================================================================

26.04.27

# variable 타입
# 1. String (문자열 type)
variable "vpc_name" {
    type        = string                # option (type을 명시적으로 지정)
    description = "vpc 이름 지정"        # option (설명)
    default     = "lecture-vpc"         # 기본값
}
# 2. Number (숫자 type)
variable "instance_count" {
    type        = number
    description = "생성할 인스턴스의 개수입니다"
    default     = 3
}
# 3. List (배열 type)
variable "avail_zones" {
    type        = list(string)
    description = "사용할 가용영역 리스트"
    default     = [ "ap-northeast-2a", "ap-northeast-2c", "ap-northeast-2d" ]
}
# 4. Map (dict 형태)
variable "common_tags" {
    type = map(string)
    description = "모든 리소스에 공통으로 붙일 태그"
        default = {
      env       = "dev"
      project   = "terraform-study"
      owner     = "kim"
    }
}
# 5. bool (논리 type)
variable "is_production" {
    type = bool
    description = "운영환경이면 true, 개발환경이면 false"
    default = false
}
# 6. number, string, bool type 을 담을 수 있는 object type 선언
type = object({
	num = number
	name = string
	is_man = bool
})
default = {
	num = 1
	name = "kim"
	is_man = true
}



# 변수에 저장된 내용 출력
output "debug06_list_all" {
    value = join(",", var.avail_zones) # type        = list(string)
}

output "debug07_map_value" {
    value = "프로젝트 환경은 ${var.common_tags.env}"
}

output "debug07_map_value2" {
    value = "프로젝트 환경은 ${var.common_tags["owner"]}"
}

output "debug01_user_list" {
    # 배열에 저장된 item을 그대로 출력
    value = [for item in var.user_list : item]
}

output "debug02_user_list2" {
    # 배열에 저장된 item(문자열)을 대문자로 변환해서 출력
    value = [for item in var.user_list : upper(item)]
}

output "debug03_user_list3" {
    # 배열에 저장된 item(문자열)의 길이가 4보다 작은 값만 출력 (필터링이 가능하다)
    value = [for item in var.user_list : item if length(item) <= 4]
}

output "debug04_user_list4" {
    # { 키 => 값 } 형태로 결과가 나오며, 중괄호 { }를 사용합니다.
    value = { for name in var.user_list : name => "IAM-USER-${name}"}
}

# 반복문 돌면서 index 값 활용해 보기
output "debug05_user_list5" {
    # for 인덱스, 값 두개를 인자로 받습니다.
    value = [ for index, item in var.user_list : "${index+1} 번째 사용자: ${item}"]
}

# 복합 활용
output "debug06_user_list6" {
    # 인덱스를 key 값, item을 value 값으로 가지는 map 만들기
    # 인덱스가 문자열로 변환되어서 key 값으로 지정된다.
    value = { for index, item in var.user_list : index => item}
}

# 여러줄의 문자열을 편하게 구성하기
output "debug_07_multiline" {
    # <<- 기호를 쓰면 좌측의 공백이 알아서 제거가 된다.
    # EOF 는 마음대로 정할 수 있다. 끝날때만 동일한 문자열로 끝나면 된다.
    value = <<-EOF
        #!/bin/bash
        dnf update -y
        dnf install -y nginx
        systemctl enable nginx
        systemctl start nginx
    EOF
}

=====================
26.04.28

ec2 생성
인벤토리 파일
cfg 파일(ansible.cfg) 만들어져야한다

delay 30 해야한다

playbook실행!


main.tf
# public ip 를 이용해서 inventory.yml 파일 만들기
resource "local_file" "ansible_inventory" {
    # 파일의 경로와 파일명
    filename = "${path.module}/inventory.yml"
    # 파일의 내용을 map 객체를 이용해서 구성하기
    content = yamlencode({
        all = {
            hosts = {
                "${aws_instance.my_ec2.public_ip}" = {
                    ansible_user = "ec2-user"
                    ansible_ssh_private_key_file = "${path.module}/lecture-key.pem"
                }
            }
        }
    })
}

# ansible.cfg 파일 생성
resource "local_file" "ansible_config" {
    filename = "${path.module}/ansible.cfg"
    # inventory 파일의 경로와 ssh 보안 확인(Host key Checking)을 자동으로 설정
    content = <<-EOF
        [defaults]
        inventory = ./inventory.yml
        host_key_checking = False
    EOF
}

# 1. 인프라 생성후 ansible play book 을 실행 가능한 시간 만큼 대기한다.
resource "terraform_data" "wait_for_instance" {
    # 서버, 인벤토리, 설정 파일이 모두 준비된 이후에 이 블럭이 실행되도록 순서 보장
    depends_on = [aws_instance.my_ec2, local_file.ansible_inventory, local_file.ansible_config]

    # ec2 인스턴스의 id가 변경된다면 다시 대기 실행하도록 방아쇠를 설치한다 ()
    # 즉 ec2가 새롭게 만들어지면 이블럭이 다시 실행되고 결과적으로 sleep 30 이 다시 실행된다. 
    triggers_replace = aws_instance.my_ec2.id

    # local computer (rocky linux)에서 실행할 명령
    provisioner "local-exec" {
        command = "sleep 30"
    }
}

# 2. ansible 플레이북 실행
resource "terraform_data" "ansible_run" {
    depends_on = [ terraform_data.wait_for_instance ]

    # ec2가 바뀔때 또다시 ansible playbook을 실행하도록 여기에 방아쇠를 걸어 놓는다.
    triggers_replace = aws_instance.my_ec2.id

    provisioner "local-exec" {
        command = "ansible-playbook site.yml"
    }
}
==============================================================
26.04.30
terrform.tfvars(default파일)->  variables.tf -> locals -> main.tf


서버리스 구조
s3 bucket: index.html
lambda: python, nodejs, java
dynamo db: aws가제공하는 db
'''