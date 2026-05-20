'''
alb 생성시 4~5분 걸린다.

alb 리스너 -> alb(acm) -> 대상그룹 -> (asg) -> ec2

ec2는 attachment 필요
asg는 attachment 불필요
    # ALB 의 target arn 을 여기에 등록한다.
    target_group_arns = [aws_lb_target_group.web_tg.arn]


# Route 53 도메인 장부 정보 읽어오기
data "aws_route53_zone" "selected" {
  name = "${var.domain_name}."
  private_zone = false
}

# 미리 만들어서 준비된 인증서 가져오기
data "aws_acm_certificate" "issued_cert" {
  domain = "*.${var.domain_name}"
  statuses = ["ISSUED"]
  most_recent = true
}

# 테스트용으로 인증서의 arn 출력해 보기
output "certficate_arn" {
  value = data.aws_acm_certificate.issued_cert.arn
}

# ALB 리스너
# 80 port 로 들어오는 요청을 443 port 로 리다이렉트 시킨다 
#  HTTPS 리스너: 인증서를 달고 443 포트를 개방



'''