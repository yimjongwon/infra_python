'''
- rocky linux docker 설치

# 1단계: Podman 제거 (충돌 방지)
sudo dnf remove -y podman buildah

# 2단계: 도커 공식 리포지토리 등록 (길 뚫기)
sudo dnf install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf makecache

# 3단계: 도커 엔진 및 최신 플러그인 설치
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 4단계: 서비스 활성화 및 자동 시작 설정
sudo systemctl enable --now docker

# 5단계: 현재 사용자에게 도커 권한 부여
sudo usermod -aG docker $USER
newgrp docker # 바로 적용
groups  # 그룹확인

[user1@mgmt ~]$ docker --version
Docker version 26.1.3, build b72abbb

docker를 실행하려면 관리자 권한이 필요하다

- docker hub 에 회원 가입을 한다
https://hub.docker.com/

'''