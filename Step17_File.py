import os


if __name__ == "__main__" :
    #현재 작업 폴더의 경로 os.getcwd()
    print(os.getcwd())
    #파일 구분자 윈도우:\, linux:/
    print(os.sep)
    r'''
        현재 memo.txt 파일은 C:\playground\python_basic\memo.txt 의 경로에 존재한다.
        해당 경로를 문자열로 만들어 보기
    '''

    #읽어올 파일의 절대경로 구성
    #os.path.join() 을 이용하면 window에서는 역슬레시로 조합하고 linux에서는 슬레시로 조합
    path:str = os.path.join(os.getcwd(), "memo.txt")
    print(path)

    #with 구문이용해서 읽기전용(r) 열기
    with open(path, "r", encoding="utf-8") as f:
        #파일에서 문자열 읽기
        result = f.read()
        print(result)