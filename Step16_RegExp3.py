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