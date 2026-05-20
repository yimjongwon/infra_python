'''
26.05.08
s3
tfstate를 관리
dynamo db
사용중일때 lock state 관리

required_version = ">= 1.14.0" # github action 에서 에러나지 않게 

github_action: 
깃허브->settings->Secrets and variables->Actions
1. AWS_ACCESS_KEY_ID
2. AWS_SECRET_ACCESS_KEY
3. SSH_PRIVATE_KEY

/home/user1/github_action/test01/.github/workflows: 정해진 이름

- deploy.yml
name: "Terraform & Ansible CI/CD"
on:
  push:
    branches: ["master"] # master 브렌치에 push 가 될때마다 실행하겠다는 의미
jobs:
  deploy:
    runs-on: ubuntu-latest # 최신 ubuntu machine 을 잠시 빌려서 아래의 작업을 수행해겠다는 의미
    # unbuntu machine 의 환경변수에 넣어줄 값을 셋팅하는 설정
    # 우리가 mgmt 서버에  aws configure 를 실행해서 키를 등록했듯이  1 회용 ubuntu 서버에도 동일한 작업을 해준다
    # job 안의 모든 step 에서 등록된 aws 키를 공통으로 사용하게 된다.
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }} # 이게 동작하기 위해서는 github 에 secrets 가 등록이 되어 있어야한다
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    steps:
      # 1. 소스코드 체크아웃
      - uses: actions/checkout@v5
     
      # 2. terraform 환경 구성
      - name: setup Terraform
        uses: hashicorp/setup-terraform@v4
     
      # 3. init & apply 실행
      - name: terraform init & apply
        run: |
          terraform init
          terraform apply --auto-approve


      # 4. ansible 용 key setting
      - name: setup ssh key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
      # 5. ansible playbook 실행
      - name: run ansible playbook
        run: |
          # terraform 이 이미 inventory.yml 과 ansible.cfg 를 현재 디렉토리에 만들어 놓았습니다.
          ansible-playbook nginx_setup.yml


- destroy.yml
name: "Terraform Destroy"
on:
  workflow_dispatch: # github action 텝에서 수동 실행 버튼을 만들어 준다.
jobs:
  terraform-destroy:
    runs-on: ubuntu-latest
    env:
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    steps:
      - uses: actions/checkout@v5


      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v4


      - name: Terraform Init
        run: terraform init


      - name: Terraform Destroy
        run: terraform destroy --auto-approve


        
==================================================================
26.05.19

name: "Packer AMI 만들기"
on:
  push:
    branches:
      - master # master 브랜치의 push 하면서
    paths:
      - "packer/**" # packer/ 하위경로에 변화가 있을때 동작하게 한다.
  workflow_dispatch: # 원할때 deploy 할 수 있는 옵션
jobs:
  packer_build: # 마음대로 가능
    runs-on: ubuntu-latest # 잠시빌려쓰는 ubuntu
    name: "Build AMI with packer & ansible"
    steps:
      - name: Checkout Repository # github 저장소로부터 소스코드 가져오기
      - name: Setup Packer # ubuntu 에 packer 설치
      - name: Aws Configure # aws 인증정보 제공
      - name: Packer Init & Build # 초기화와 빌드를 한번에
      - name: Setup Terraform # 테라폼 설치
      - name: Terraform Init & Apply # ./terraform 안에 있는 terraform 자원을 init, apply

코드 문법 오류 쉽게 찾는 방법
- 깃헙액션 코드의 문법적 오류 검사
https://github.com/rhysd/actionlint
- 온라인으로도 제공
https://rhysd.github.io/actionlint


'''