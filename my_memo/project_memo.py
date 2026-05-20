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


main브랜치에서 기능브랜치 만들것


- ec2에 cloudwatch 기능 추가
1. Route 53 Health Check 수정

# 수정된 Route 53 Health Check
resource "aws_route53_health_check" "onprem_check" {
  type                            = "CLOUDWATCH_METRIC"
  cloudwatch_alarm_name           = aws_cloudwatch_metric_alarm.onprem_health_alarm.alarm_name
  cloudwatch_alarm_region         = "ap-northeast-2"
  insufficient_data_health_status = "Unhealthy" # 데이터가 없으면 문제가 있는 것으로 간주

  tags = { Name = "onprem-tailscale-check" }
}

# CloudWatch 알람 추가 (EC2가 보내주는 데이터를 기반으로 판단)
resource "aws_cloudwatch_metric_alarm" "onprem_health_alarm" {
  alarm_name          = "onprem-health-alarm"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "OnPremStatus" # EC2가 보낼 메트릭 이름
  namespace           = "Custom/OnPrem"
  period              = "60"
  statistic           = "SampleCount"
  threshold           = "1" # 1분 동안 데이터가 하나도 안 들어오면 알람 발생
  alarm_description   = "This alarm monitors on-premise server availability via Tailscale"
}

2. EC2 보안 그룹 수정

# 기존 ec2_sg에 추가
resource "aws_security_group_rule" "allow_tailscale" {
  type              = "ingress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["100.64.0.0/10"] # Tailscale 대역 허용
  security_group_id = aws_security_group.ec2_sg.id
}

3. EC2에 IAM 역할(Role) 부여 (중요)

# IAM 정책 생성 및 역할 연결 (생략된 부분은 표준 IAM 설정 필요)
# EC2에 CloudWatch:PutMetricData 권한이 반드시 있어야 함

# 3-1. '사원증' 자체를 정의 (어떤 서버가 쓸 수 있는지)
resource "aws_iam_role" "ec2_cloudwatch_role" {
  name = "azas-ec2-cloudwatch-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = { Service = "ec2.amazonaws.com" }
      },
    ]
  })
}

# 3-2. '사원증'에 들어갈 권한 내용 (CloudWatch에 데이터를 쓸 수 있는 권한)
resource "aws_iam_role_policy_attachment" "cloudwatch_policy" {
  role       = aws_iam_role.ec2_cloudwatch_role.name
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy" 
}

# 3-3. '사원증'을 찍을 수 있는 리더기(인스턴스 프로파일) 생성
resource "aws_iam_instance_profile" "ec2_profile" {
  name = "azas-ec2-profile"
  role = aws_iam_role.ec2_cloudwatch_role.name
}

# 3-4. 실제 EC2 서버(app_server)에 '사원증 리더기' 장착
resource "aws_instance" "app_server" {
  # ... 기존 설정들 ...
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name # 이 부분이 핵심!
}



4. Ansible 혹은 User Data에 감시 스크립트 추가

resource "aws_instance" "app_server" {
  # ... 기존 설정 (ami, instance_type 등) ...

  # User Data 추가
  user_data = <<-EOF
              #!/bin/bash
              # 1. AWS CLI 및 필요한 도구 확인 (Amazon Linux 2023은 기본 설치됨)
              
              # 2. 감시 스크립트 생성
              cat << 'SCRIPT' > /usr/local/bin/check_onprem.sh
              #!/bin/bash
              # 온프레미스 Tailscale IP
              ONPREM_IP="100.93.36.66"
              REGION="ap-northeast-2"

              # 핑 테스트 (1번 전송, 타임아웃 2초)
              ping -c 1 -W 2 $ONPREM_IP > /dev/null 2>&1

              if [ $? -eq 0 ]; then
                # 성공 시 CloudWatch에 정상(1) 보고
                aws cloudwatch put-metric-data \
                  --metric-name OnPremStatus \
                  --namespace Custom/OnPrem \
                  --value 1 \
                  --region $REGION
              fi
              SCRIPT

              # 3. 실행 권한 부여
              chmod +x /usr/local/bin/check_onprem.sh

              # 4. 크론탭(Cron)에 등록 (1분마다 실행)
              echo "* * * * * root /usr/local/bin/check_onprem.sh" >> /etc/crontab
              
              # 5. 크론 서비스 재시작
              systemctl restart crond
              EOF

  # 중요: IAM 프로파일이 반드시 연결되어 있어야 함
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name
}


그라파나
텔레그램
sns


감마: AI 템플릿


'''