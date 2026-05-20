'''
aws의 lambda, s3, cloud front, acm, route 53, dynamodb

python 환경에서
/send_message 요청을 처리할 수 있는 end point 를 만들어 두고 대기 한다.

미미한 비용으로 로직 처리가 가능

python, nodejs, java 등등 다른 언어도 지원한다
DB 연동 가능하다(Dynamo DB:온디맨드)
RDS(mysql, oracle, postgresql)는 켜놓은 것 만으로 비용이 지출된다

lambda는 python, java(살짝 무겁다), nodejs(보통많이사용) 가능하다
java인경우 jar파일을 올려야한다

cloud front(CDN)를 통해 https가 가능하다(주소창이 복잡하다)->route53,acm으로 변경가능하다

'''