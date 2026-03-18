# 한줄 주석입니다.
'''
    여기는 여러줄 주석입니다.
    어쩌구 저쩌구...

'''

print("Step01 시작")

# python 의 여러가지 데이터 type 에 대해서 알아보자

# int type
num1 = 10
# float type
num2 = 10.1

# str type
myName = '김구라'
yourName = "해골"
ourName = """
    KT Cloud Infra
    화이팅!
"""

print(myName)

# 순서가 중요한 여러개의 데이터를 관리하고 싶다면 ...
# 내가 좋아하는 음식 목록 3가지를 하나의 변수에 순서대로 담고 싶다면...
foods = ["삼겹살", "김밥", "닭발"]
print(foods) # list


# 순서가 중요하지 않지만 여러개의 데이터를 관리하고 싶다면 ...
# 회원 1명의 정보
mem1 = {"num":1, "name":"김구라", "addr":"노량진"} # dict
print(mem1)

# 순서가 중요치 않은 데이터를 하나의 묶음으로 관리(키값 없이)
mySet = {"빨강사탕", "초록사탕", "노랑사탕"}

print(mySet)

# 특정 code 블럭을 필요한 시점에 일괄 실행하고 싶다면?
# 함수를 만들고
def store():
    print("냉장고 문 연다")
    print("물건 저장한다")
    print("냉장고 문 닫는다")
# 여기서는 바로 실행했지만 필요한 시점에 실행하면 된다.
store()
returnValue = store()

# 어떤 변수를 빈 상태로 만들고 싶다면? None
a = None
print("어떤 작업을 하고")
print("필요할때 값을 넣는다")
a = "test"

print("a값 변화")