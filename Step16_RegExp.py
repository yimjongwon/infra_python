'''
    정규표현식 (Regular Expression)

'''

import re

#대상 문자열에서 
data:str = "apple, banana, cherry"

# "a" 라는 정규표현식에 매칭되는 모든 문자열을 찾아서 list 담아서 리턴된다
result = re.findall(r"a",data)

#결과 확인
print(result)

# 대상 문자열 2
text:str = "Contact: 010-1111-2222 입니다"

m_obj = re.search(r"010-[0-9]{4}-[0-9]{4}", text)

#없으면 None, 있으면 re.Match 객체의 참조값
print(m_obj)
# .gruop()을 호출하면 매칭되는 문자열이 리턴된다.
print(m_obj.group())