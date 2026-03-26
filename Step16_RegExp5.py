import re


if __name__ == "__main__" :
    input_id = input("아이디 입력(영문자로 시작하고, 5~10 글자 이내, 특수문자 허용안함):")

    # 조건에 맞으면 "가입되었습니다" 맞지 않으면 "사용할 수 없는 아이디 입니다" 출력
    p = r'^[a-zA-Z][a-zA-Z0-9]{4,9}$' #반복 4번이상 9번이하
    print(re.search(p,input_id))
    if re.search(p,input_id):
        print("가입되었습니다")
    else:
        print("사용할 수 없는 아이디 입니다")



