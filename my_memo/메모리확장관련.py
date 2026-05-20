'''
서버를 shutdown한다음에
하드디스크를 늘린다. 20->40

- rocky linux 늘어난 용량 인식 시키기 
# 1. 파티션 확장 도구 설치 (이미 설치되어 있다면 금방 넘어갑니다)
sudo dnf install -y cloud-utils-growpart

# 2. 파티션(nvme0n1p2) 확장 (디스크 이름과 파티션 번호 '2' 사이의 띄어쓰기 주의!)
sudo growpart /dev/nvme0n1 2

# 3. LVM 물리 볼륨(PV) 업데이트 (파티션이 커졌음을 LVM에 알림)
sudo pvresize /dev/nvme0n1p2

# 4. 루트 논리 볼륨(LV)에 남은 공간 100% 할당
sudo lvextend -l +100%FREE /dev/mapper/rl-root

# 5. 파일시스템(XFS) 확장 (최종적으로 OS가 용량을 사용할 수 있게 적용)
sudo xfs_growfs /

# 6. 최종 확인
df -h 

- ubuntu  root 볼륨 확장
# 1. 파티션 확장 도구 설치 (이미 깔려있으면 금방 넘어갑니다)
sudo apt update
sudo apt install -y cloud-guest-utils

# 2. 파티션 확장 (울타리를 넓힌 땅끝까지 밀어버립니다)
# 주의: /dev/sda와 2 사이에 반드시 띄어쓰기가 있어야 합니다!
sudo growpart /dev/sda 2

# 3. 파일시스템 확장 (넓어진 파티션에 파일시스템 인테리어를 꽉 채웁니다)
# 주의: 여기서는 띄어쓰기 없이 붙여서 씁니다!
sudo resize2fs /dev/sda2

# 4. 확인
df -h /


'''