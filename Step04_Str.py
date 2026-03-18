# str type에 대해 알아보기

# 양쪽 공백이 포함되거나 포함될 가능성이 있는 문자열이 있다고 가정
text = "    Cloud Infra "

#만일 공백을 제거 하고 싶다면?
result = text.strip()

myIp = "192.168.0.2"
result2 = myIp.split(".")

#join 다시 합치기
result3 = ".".join(result2)

#특정 문자열 찾아서 대체하기
result4 = "hello mimi!".replace("mi","ma")

result5 = "python".upper()
result6 = "pYTHON".lower()

print("제거합니다")

