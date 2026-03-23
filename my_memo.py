'''
json정리
json.load(info) str->dict
json.dump(info) dict->str
yaml정리
yaml.sage_load(info) str->dict
yaml.dump(info) dict->str

git 정리
git init
git add 파일명
git add .
git commit -m "메시지"
git commit
git switch master
git checkout master
git merge lab1
git branch
git branch -d 브랜치
git branch -D 브랜치
git log --graph --oneline --all
git restore
git restore --staged:스테이지 올라간 거 취소
git reset --soft: commit 메시지 잘못 작성했을 때, add할 파일을 누락했을때
git reset --mixed: 여러개의 파일을 만들고 작업을 했는데 그중에 일부분만 
                    잘못 작성했을때
git reset --hard HEAD~ :처음부터 다시 시작하고 싶을때
git reset --hard HEAD~~

git pull origin master= git fetch origin master + git merge origin/master

-작업하다가 임시 저장하고 다른 브랜치로 이동할때
git stash -u
가상환경 정리 
PowerShell -> Set-ExecutionPolicy RemoteSigned
python -m venv venv
.\venv\Scripts\activate

- python 수업 소스코드
https://github.com/oli999/infra_python

snippet : 커맨드 설정
-https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode

설치 정리
pip install pyyaml
pip install jinja2

# 템플릿 파일이 위치한 폴더 설정
from jinja2 import Environment, FileSystemLoader, Template

import tkinter as tk
from tkinter import messagebox


'''