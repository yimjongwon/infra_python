# 콘솔창으로부터 문자열 입력 받기

input_msg = input("메시지 입력:")

print(f"입력한 메시지: {input_msg}")


input_name : str = input("이름 입력:")
input_addr: str = input("주소 입력:")

print(f"이름:{input_name} 주소:{input_addr}")

#문자열로 입력 받은후
input_age: str = input("나이 입력:")
# 숫자로 변경해서 1을 더한값을 얻어낸다.
age:int = int(input_age) + 1

print("당신은 내년에 {age} 살 입니다")