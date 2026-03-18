# list type에 대해 알아보자
"""
    1. 순서가 있다
    2. 여러 type의 데이터를 저장할 수 있다
    3. 값 변경 가능
"""

nums = [10, 20, 30]
names = ["김구라", "해골", "원숭이"]

datas=[10, "xxx", True]
datas.append(40)

# len() builtin 함수를 이용해서 list 의 길이를 얻어낼수있다.
nums_len = len(datas)
# 인덱스에 위한 참조
name0 = names[0]

# 인덱스를 이용해서 삭제
del names[0] 

names.remove("원숭이")

# 맨마지막 index 를 삭제하면서 값을 가져오기
nums.pop()
result = nums.pop()

print("종료")