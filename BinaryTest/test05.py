source = "11110000"

print(int(source, 2))

source2 = "11110003"

result1 = set(source).issubset({"0", "1"})
result2 = set(source2).issubset({"0", "1"})

print(f"{source}가 0과 1로만 되어 있는지 여부: {result1}")
print(f"{source2}가 0과 1로만 되어 있는지 여부: {result2}")
print(f"{source}가 8자리 초과 인지 여부: {len(source) > 8}")