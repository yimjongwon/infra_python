#yaml 형식의 문자열 다루기

#yaml 문자열을 다룰때는 외부 모듈을 pip로 설치를 해서 inport로 해야한다.
import yaml


info = '''
name: 이정호
addr: 노량진
foods: 
  - 맥주
  - 치킨
isMan: true
body:
  weight: 75
  height: 175
'''

#검색 혹은 ai의 도움을 받아서 info에 들어 있는 문자열을 
# dict type으로 바꾸세요
#그런 다음 dict에 들어 있는 내용을 확인후 
# 다시 dict에 있는 내용을 이용해서 yaml 문자열 형식으로 변환해보세요.

result = yaml.safe_load(info)
print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])
print(result["isMan"])
print(result["body"])
print(result["body"]["weight"])
print(result["body"]["height"])

result2 = yaml.safe_dump(result)
print(result2)
print("종료")


