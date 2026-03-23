# 비트연산 or, xor, not
a = 0b1100
b = 0b1010

# bit or 연산
print(bin(a|b))


# bit xor 연산
print(bin(a^b))


# bit not 연산 ~n -> - (n+1)
print(bin(~a))

# 이쁘게 보고싶으면
print(bin(~a & 0xF))