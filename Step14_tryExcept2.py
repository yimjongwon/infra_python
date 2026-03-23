
if __name__ == "__main__" :
    try:
        num1_str: str = input("젯수 입력:")
        num2_str: str = input("피젯수 입력:")
        #숫자로 형변환
        num1: int = int(num1_str)
        num2: int = int(num2_str)
        result = num2/num1
        #결과  출력
        print(f"{num2} 를 {num1}으로 나눈 결과 값 : {result}")
    except Exception as e: #exception type이다.
        print("어떤 에러가 발생했습니다.", e)
    else:
        pass
    finally:
        pass

    print("중요한 마무리 작업을 합니다")