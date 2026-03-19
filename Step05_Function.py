"""
    function type

    - 특정시점에 여러줄의 code 일괄실행하고하고자 할때 사용한다.
    - 함수도 data 이다
    - 함수안에 저장된 code를 일괄실행하는 것을 함수를 call 한다고 한다.
    - 함수는 저장된 code를 다 실행하고 나면 원래 call 했던 위치로 실행의 흐름이 넘어온다.
    - call 했던 위치로 돌아오면서 어떤 data를 반드시 가져온다.
"""

def test1():
    print("test1() 호출됨")
    
test1()
result1 = test1()

#매개변수 입력받은 경우
def test2(arg):
    print("전달 받은 내용", arg)
    print(f"전달 받은 내용: {arg} ")

test2(None)
test2(10)    
test2("kim")

# 값(숫자)을 2개 전달 받아서 전달 받은 두수의 합을 출력하는 함수
def print_sum(num1: int, num2: int):
    sum = num1+num2
    print(f"{num1} + {num2} = {sum}")

print_sum(10, 20)

def print_info(name: str, addr: str):
    print(f"이름: {name} 이고 주소는 {addr}")
   
print_info("김구라","노량진")
print_info(addr="행신동", name="해골")

print("종료")