'''
==============================================================================
git 정리
git init
git add 파일명
git add .
git commit -m "메시지"
git commit
git remote add origin https://github.com/yimjongwon/Fastapi_test03.git

git status
git switch master
git checkout master
git merge lab1
git branch
git branch -d 브랜치
git branch -D 브랜치
git log --graph --oneline --all
# git 변경사항 취소
git restore .
git restore --staged:스테이지 올라간 거 취소
git reset --soft: commit 메시지 잘못 작성했을 때, add할 파일을 누락했을때
git reset --mixed: 여러개의 파일을 만들고 작업을 했는데 그중에 일부분만 
                    잘못 작성했을때
git reset --hard HEAD~ :처음부터 다시 시작하고 싶을때
git reset --hard HEAD~~

git pull origin master= git fetch origin master + git merge origin/master

-작업하다가 임시 저장하고 다른 브랜치로 이동할때
git stash -u
git stash pop 기록삭제하고 되돌리기
git stash apply 기록저장하고 되돌리기

# git 변경사항 취소
git restore .

# untracked file 도 제거 하기(한번도 commit 하지 않은 파일일때 쓰인다)
git clean -fd
==============================================================================

feature/기능구현
fix /기능 복구 (버그 잡기)
bugfix/xxx


1. pull request (merge하는과정)
2. git pull origin master (내려받고)
3. git branch -d fix/new_post (branch삭제하기)

 git remote -v : 원격 저장소 목록 확인

깃허브에 ssh 접속하는법
1.윈도우 cmd
ssh-keygen -t ed25519 -C "awosung00@naver.com"
2. 공개키를 깃허브 setting->SSH and GPG keys에 등록한다.
3. 
git remote -v :목록확인
git remote rm origin : 저장소 삭제
git remote add origin git@github.com:yimjongwon/Fastapi_test03.git: ssh로 추가
git push origin feature/post_update : 브랜치 정리

저장소 Collaborators가 사용할 수 있는 권한을 제어가능하다.
깃허브 Settings->Rules->Rulesets
Add bypass 랑 Target branches가있고
Branch rules에는 Require a pull request before merging설정을 해야한다.

처음 가져올때는 clone실행할것. 그이후 pull


개발된 브랜치를 push하기 전에
master의 이력을 pull 받은 다음
개발된 브랜치를 merge해서
충돌된 부분이 있으면 해결한다음
개발된 브랜치를 push하고
pr을 날려야 merge 가능한 상태가 된다


작업하던 브랜치에서 
git add . git commit 
git switch master
git pull git@github.com:juhy0987/azas_application_server.git
git switch feature/기능
작업하던 브랜치에서 git merge  master 


[user1@mgmt terraform]$ git add .
[user1@mgmt terraform]$ git commit -m "[FEAT]: Route 53 호스팅 영역 및 ACM  인증서 추가"
[user1@mgmt terraform]$ git branch
* feature/#11/alb_terraform
  main
[user1@mgmt terraform]$ git switch main
[user1@mgmt terraform]$ git pull origin main
[user1@mgmt terraform]$ git switch feature/#11/alb_terraform 
[user1@mgmt terraform]$ git merge main
[user1@mgmt terraform]$ git push -u origin feature/#11/alb_terraform 

합쳐지면 브랜치삭제
git branch -d "feature/#11/alb_terraform"
브랜치 목록확인
[user1@mgmt terraform]$ git branch -r


======================================================
26.04.29
[user1@mgmt terraform_example]$ git init


[user1@mgmt ~]$ git clone git@github.com:oli999/terraform_example.git terraform_example_teacher
.terraform.lock.hcl 파일은 삭제하지말기
terraform init
한 번에 캐시 삭제하는 마법의 명령어
find . -name ".terraform" -type d -exec rm -rf {} +
find .: 현재 폴더(.)부터 하위 폴더를 모두 뒤집니다.

-name ".terraform": 이름이 .terraform인 것을 찾습니다.
-type d: 파일이 아닌 '디렉토리(폴더)'만 골라냅니다.
-exec rm -rf {} +: 찾아낸 폴더들을 하나씩 rm -rf 명령어로 삭제합니다.
df
'''