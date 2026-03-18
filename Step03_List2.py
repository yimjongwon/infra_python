#list type에 대해서 알아보기

nums = [10, 20, 30, 40, 50]
names = ["kim", "park", "jo", "oh", "choi"]

# list에 들어 있는 데이터를 앞에서부터 참조하면서 
# 어떤 동작을 할 일들이 많이발생한다.

#nums에 저장되어 있는 데이터를 순서대로 참조하면서 콘솔창 출력
for item in nums:
    print(item)
#names에 들어 있는 데이터를 앞에서부터 순서대로 참조하면서 출력
for item in names:
    print("names 를 순서대로 출력중...")
    print(item)

r1 = range(5)
r2 = range(10)

print(r1, r2)

for item in range(5):
    print(item)

result2 = range(len(names))

#반복문 돌면서 인덱스도 같이 필요하다면...
for i in range(len(names)):
    print("list의 index와 함께 출력합니다")
    print(i, names[i])

print("종료")