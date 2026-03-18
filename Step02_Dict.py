# dict type에 대해 알아보자

#회원 1명의 데이터
mem1 = {"num":1, "name":"김구라", "isMan":True}
#회원 1명의 데이터(사용이 불편한 경우)
#info1 = [1, "김구라", True]
print(mem1["num"], mem1["name"], mem1["isMan"])

# dict 안에 내용을 참조해서 변수에 담기
a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

# dict 안의 내용을 수정하기

mem1["num"] = 2
mem1["name"] = "임종원"
mem1["isMan"] = False

# 특정 key 값으로 저장된 내용 삭제
del mem1["isMan"]

# 모든 값 삭제
mem1.clear()


print("종료됩니다")

# 참과 거짓을 나타내는 date type (Bool), isxxx, canxxx
isMan=True
isWoman=False
isDifferent=True
isRun=False
canEat=True