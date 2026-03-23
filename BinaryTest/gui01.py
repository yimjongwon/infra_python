# ui ToolKit 을 사용할 수 있는 interface 객체 import 하기
import tkinter as tk

def clicked():
        try:
            print("버튼을 클릭했습니다")
            # Entry(입력창)에 입력한 문자열 읽어오기
            num = int(num_entry.get())
            if(0<=num<=255):
                result = f"{num:08b}"   
                label2.config(text=f"10 진수-> 2진수 변경값: {result}")
            else:
                label2.config(text=f"0~255 사이의 값을 입력하세요.")
        except ValueError:
            label2.config(text=f"숫자만 입력하세요.")
        except Exception as e:
            label2.config(text=f"다시 입력하세요.")

if __name__ == "__main__" :

    # root 창 생성
    root = tk.Tk()

    #제목 설정
    root.title("나의 app")

    #창의 크기
    root.geometry("400x300")

    #레이블 
    label = tk.Label(root, text="안녕하세요! python GUI 입니다")
    label.pack(pady=20)

    #입력창
    num_entry = tk.Entry(root, font=("Arial", 12))
    num_entry.pack(pady=5)
    num_entry.focus() #포커스 주기

    #버튼
    btn = tk.Button(root, text="전송", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    label2 = tk.Label(root, text="결과...")
    label2.pack(pady=20)

    #창이 닫힐때 까지 무한 대기
    root.mainloop()
