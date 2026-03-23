# python 에서 2진수 다루기

num1 = 0b1010

result = num1 + 5
print(result)

# 10 진수를 2진수로 변환
num2 = 150
result2:str = bin(num2)
print(result2)

print("-----------")

line = "abcde12345"
print(line[4:10])

# 0b제외한 문자열
print(result2[2:])