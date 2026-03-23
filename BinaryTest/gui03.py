# ui ToolKit 을 사용할 수 있는 interface 객체 import 하기
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했습니다")
    # Entry(입력창) 에 입력한 문자열 읽어오기
    input_value=entry.get().strip() # 좌우 공백 제거 strip()
    #빈 값일 경우 안내 문구 표시
    if not input_value:
        return #함수를 호출한 곳으로 실행의 흐름을 돌려준다(함수를 여기서 종료한다)
    
    try:
        # 만일 0과 1 이외의 문자를 입력 했다면 함수 종료 시키기
        if not set(input_value).issubset({"0","1"}):
            result_label.config(text="0 과 1만 입력 가능 합니다.", fg="red")
            return
        # 8 자리 인지 확인
        if len(input_value) > 8:
            result_label.config(text="8 자리 까지만 입력 가능 합니다", fg="red")
            return
        # 2 진수 문자열을 10진수 정수로 변환
        num=int(input_value, 2)
        # 결과 표시
        result_label.config(text=f"10진수:{num}", fg="blue")
        
    except Exception as e:
        result_label.config(text="숫자만 입력 가능 합니다", fg="red")
        

if __name__ == "__main__" :

    # root 창 생성
    root = tk.Tk()

    #제목 설정
    root.title("나의 app")

    #창의 크기
    root.geometry("400x300")

    #레이블 
    label = tk.Label(root, text="2진수 8자리를 10진수로 변환")
    label.pack(pady=20)

    #입력창
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() #포커스 주기

    #버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    #결과 값을 출력할 Label
    result_label = tk.Label(root, text="결과...")
    result_label.pack(pady=20)

    #창이 닫힐때 까지 무한 대기
    root.mainloop()
