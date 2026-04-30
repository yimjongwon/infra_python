'''
26.04.24

[user1@mgmt ~]$ sudo rpm -ivh cloudflared-linux-x86_64.rpm
[user1@mgmt ~]$ cloudflared --version
[user1@mgmt ~]$ cloudflared tunnel login
[user1@mgmt ~]$ cloudflared create edu-tunnel

준비1. cloudflare 설치 rocky

# 1. 최신 cloudflared RPM 패키지 다운로드
curl -L -O https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-x86_64.rpm

# 2. 패키지 설치 (관리자 권한 필요)
sudo rpm -ivh cloudflared-linux-x86_64.rpm

# 3. 설치 정상 확인 (버전이 출력되면 성공!)
cloudflared --version



0. 도메인등록하기

1. cloudflared 로그인 (vmware 에서) 

[user1@mgmt ~] cloudflared tunnel login 

- 기존에 domain 을 다른 용도로 사용한적이 있으면 과거 정보 삭제하기 


2. 터널 만들기
[user1@mgmt ~] cloudflared tunnel create edu-tunnel


3. 설정 파일(config.yml) 작성

# 주의! [ ] 대괄호는 넣지 않는다. id 만 넣기  
tunnel: e4edbba0-fe64-4dc4-9c3c-ca30070aef94
credentials-file: /home/user1/.cloudflared/e4edbba0-fe64-4dc4-9c3c-ca30070aef94.json

ingress:
 # 루트 도메인(cloud-study.site)으로 들어오면 Nginx(80포트)로 보내라!
  - hostname: cloudyim.store
    service: http://localhost:80

  # 1번: FastAPI 서버 (8000번 포트)
  - hostname: api.cloudflare.com
    service: http://localhost:8000

  # 2번: 테스트 서버 (8080번 포트)
  - hostname: test.cloudflare.com
    service: http://localhost:8080

  # 3번: 나머지 모든 트래픽은 404 처리
  - service: http_status:404




4. 메인 도메인 연결
cloudflared tunnel route dns edu-tunnel cloud-study.site

5. API 서브도메인 연결
cloudflared tunnel route dns edu-tunnel api.cloud-study.site

6. 테스트 서버 서브도메인 연결
cloudflared tunnel route dns edu-tunnel test.cloud-study.site


- 테스트용 ngnix 설치및 시작

# 1. nginx 설치
 sudo dnf install nginx -y 

# 2. 서비스 시작 및 자동 실행 
sudo systemctl start nginx 
sudo systemctl enable nginx 

# 3. 상태 확인
 sudo systemctl status nginx 



7. 터널을 가동 임시 테스트 
cloudflared tunnel run edu-tunnel
https://acornacademy.shop  등록한 도메인 이름을 웹브라우저에 입력해 본다.
테스트후 ctrl+c 해서 종료 


8. 테스트 성공후 데몬 서비스 등록
sudo mkdir -p /etc/cloudflared

sudo cp  ~/.cloudflared/config.yml   /etc/cloudflared/
sudo cp  ~/.cloudflared/*.json   /etc/cloudflared/
sudo cp  ~/.cloudflared/cert.pem  /etc/cloudflared/

# 앞서 발급받았던 터널 설정 파일(config.yml) 위치를 잡아주며 서비스로 등록합니다.
sudo cloudflared service install


기존 서비스 삭제
sudo cloudflared service uninstall
표준 서비스로 다시 설치
sudo cloudflared service install

9. 서비스 시작 및 부팅 시 자동 실행 적용
sudo systemctl start cloudflared
sudo systemctl enable cloudflared
sudo systemctl status cloudflared  


'''