import re

logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]
# logs 에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력해 보세요.
for p in logs:
    if re.match(r'^\[(WARN|ERROR)\]',p):
        #r'^\[ERROR\]|^\[WARN\]'
        print(p)

pattern = r"^\[(WARN|ERROR)\]"
for tmp in logs:
    if re.search(pattern, tmp):
        print(tmp)


'''
^: 문자열의시작
$: 문자열의 끝
.: 임의의 한 문자(줄바꿈 제외)
*: 앞의 문자가 0번 반복
+: 앞의 문자가 1번 이상 반복
?: 앞의 문자가 0번 또는 1번 존재
[ ]: [abc] 문자중 하나
|: OR
\d:숫자[0-9]
\D:숫자아닌거[^0-9]
\w:문자+숫자+_[a-zA-Z0-9_]-ID규칙에 많이 사용
\s:공백 문자 (스페이스, 탭)
'''

# 첫글자가 W or A or R or N 인지를 검증할수 있는 정규 표현식
pattern1 = r"^[WARN]"
#  [WARN] 으로 시작하는지 검증할수 있는 정규 표현식
pattern2 = r"^\[WARN\]"
#  [ERROR] 으로 시작하는지 검증할수 있는 정규 표현식
pattern3 = r"^\[ERROR]\]"
# WARN or ERROR 로 시작하는지 검증할수 있는 정규 표현식
pattern4 = r"^(WARN|ERROR)"
# [WARN] or [ERROR] 로 시작하는지 검증할수 있는 정규 표현식
pattern = r"^\[(WARN|ERROR)\]"