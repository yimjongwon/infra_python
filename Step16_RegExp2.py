import re

# 대상 문자열
text = "Contact: 010-1234-5678, Email: test@gmail.com, Year: 2026"

# 1. re.match() : 문자열의 '처음'부터 확인 (시작이 안 맞으면 None)
m = re.match(r'^Contact', text) 
if m :
    print(m.group())

# 2. re.search() : 문자열 '전체'에서 첫 번째 매칭되는 곳 찾기
s = re.search(r'\d{4}', text) # '1234' 반환
if s :
    print(s.group())

# 3. re.findall() : 매칭되는 모든 것을 '리스트'로 반환 (핵심!)
f = re.findall(r'\d+', text) # ['010', '1234', '5678', '2026']
if f :
    print(f)

# 4. re.sub() : 패턴을 찾아 다른 문자열로 치환 (데이터 정제)
sub = re.sub(r'\d+', 'NUMBER', text) # 숫자를 모두 'NUMBER'로 교체
print(sub)