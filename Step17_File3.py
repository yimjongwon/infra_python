import os


if __name__ == "__main__" :
    #읽어올 text 문서의 경로 구성하기
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")

    with open(letter_path, "r", encoding="utf-8") as f:
        # 문자열 한줄씩 읽기
        print(f.readline()) #개행기호가 포함되어 있다
        print(f.readline())
        print(f.readline().strip()) # 좌우공백이나 개행기호 없애고 싶다면 .strip()
        print(f.readline().strip())

        print("-------- 반복문 처리 ----------")

        with open(letter_path, "r", encoding="utf-8") as f:
            for line in f:
                print(line)