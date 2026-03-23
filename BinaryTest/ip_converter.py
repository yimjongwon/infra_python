# BinaryTest/ip_converter.py

import tkinter as tk
from tkinter import messagebox

def convert_ip(event=None):
    """
    입력창(Entry)에 입력된 IPv4 주소를
    8비트 2진수 형태로 변환하여 결과 라벨에 표시하는 함수
    """
    ip_str = entry.get().strip()
    
    if not ip_str:
        result_label.config(text="IP를 입력하세요", fg="gray")
        return

    try:
        parts = ip_str.split('.')
        
        # IPv4 옥텟 개수 검증
        if len(parts) != 4:
            raise ValueError
            
        binary_list = []

        for p in parts:
            val = int(p)

            # 0 ~ 255 범위 검증
            if 0 <= val <= 255:
                binary_list.append(f"{val:08b}")
            else:
                raise ValueError
        
        # 결과 결합 및 출력
        result = " . ".join(binary_list)
        result_label.config(text=result, fg="blue")
        
    except ValueError:
        result_label.config(text="올바른 IPv4 형식이 아닙니다 (0~255)", fg="red")

# =========================================================
# 메인 실행부

if __name__ == "__main__":
    # 메인 윈도우 생성
    root = tk.Tk()
    root.title("IP to Binary Real-time Converter")
    root.geometry("500x250")


    # 1. 안내 문구
    instruction = tk.Label(
        root,
        text="IP 주소를 입력하세요 (실시간 변환)",
        font=("Arial", 12)
    )
    instruction.pack(pady=10)


    # 2. 입력창 (전역 변수로 선언되어 함수에서 참조 가능)
    entry = tk.Entry(
        root,
        font=("Courier", 18),
        justify='center'
    )
    entry.pack(pady=10, padx=20, fill='x')


    # 키 입력 이벤트 연결 (실시간 변환 핵심)
    entry.bind("<KeyRelease>", convert_ip)


    # 3. 결과 영역 제목
    result_title = tk.Label(
        root,
        text="[ 8비트 2진수 결과 ]",
        font=("Arial", 10, "bold")
    )
    result_title.pack(pady=5)


    # 4. 실제 결과를 보여주는 라벨
    result_label = tk.Label(
        root,
        text="00000000 . 00000000 . 00000000 . 00000000",
        font=("Courier", 14, "bold"),
        fg="blue"
    )
    result_label.pack(pady=10)


    # 초기 포커스 설정
    entry.focus()


    # 이벤트 루프 시작
    root.mainloop()
