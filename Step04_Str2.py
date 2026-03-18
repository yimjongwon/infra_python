'''
    여러분의 이름과 주소 좋아하는 음식 2가지를 작성해서 채팅창에 올려보세요
    json, xml, yaml ...

    json은 javascript 객체 표기법을 따르는 문서 형식
'''
# info는 str type이긴한데 문자열이 특별한 형식(json)을 띄고 있다.
import json


info = '''{
    "name":"임종원",
    "addr":"경기도",
    "foods":["맥주","치킨"]
}'''

# result는 str(json형식) 문자열의 python의 dict로 변경된 값을 가지고 있다.
result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

# result2는 dict에 저장된 데이터를 json 문자열로 변환
result2 = json.dumps(result)


print("종료")