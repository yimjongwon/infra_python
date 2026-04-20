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
'''