import os
import re


if __name__ == "__main__" :
    #문자열 한줄 한줄을 저장할 list
    updated_lines=[]

    #SELINUX=xxxx pattern의 문자열을 찾을 정규 표현식
    pattern=r"^SELINUX=[a-zA-Z]+"

    #읽어들일 파일의 경로
    file_path=os.path.join(os.getcwd(), "config.txt")
    #읽기전용 읽어들이기
    with open(file_path, "r", encoding="utf-8") as f:
        #반복문 돌면서 문자열을 한줄씩 읽어들인다
        for line in f:
            #만일 pattern에 매칭되는 line이면
            if re.match(pattern, line):
                 #SELINUX=xxxx 를  #SELINUX=disabled 로 치환(subtitution)하기
                result=re.sub(pattern,"SELINUX=disabled",line)
                #바꾼 결과값을 list에 추가(저장) 하기
                updated_lines.append(result)
            else:
                #매칭되는게 없다면 그대로 추가
                updated_lines.append(line)
    print(updated_lines)

    #list에 저장된 문자열을 이용해서 file을 새로 만든다.
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)
    print("config.txt 파일을 수정 했습니다")