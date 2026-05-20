'''
26.05.15

route53
호스팅영역

route 53 에서 구입하지 않은 domain 을 등록해서 사용하는 방법
다른곳에서 구입한 본인 소유의 domain 이름을 입력한다
(route53에서 구입한 것은 자동으로 호스팅 영역에 등록된다)
ns 4줄을 가비아에 가서 나온대로 정보 입력해서 수정해야한다




# 네임서버 설정 실시간 확인 하는 방법
[user1@mgmt test09_alb]$ nslookup -type=ns cloudyim.store
Server:         100.100.100.100
Address:        100.100.100.100#53

Non-authoritative answer:
cloudyim.store  nameserver = ns-1504.awsdns-60.org.
cloudyim.store  nameserver = ns-611.awsdns-12.net.
cloudyim.store  nameserver = ns-469.awsdns-58.com.
cloudyim.store  nameserver = ns-2031.awsdns-61.co.uk.

확인했으면 인증서 발급한다


# route 53, ACM

# 1. Route 53에 호스팅 영역에 등록된 도메인 정보 조회
# 2. ACM 인증서 발급 신청
# 3. DNS 검증용 레코드 생성
# 4. 인증서 검증 대기 및 완료 (최종 상태 확인)
# 5. 발급된 인증서의 arn 확인(출력)

===============================================================


'''