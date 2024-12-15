a = 0.1 + 0.2
b = 0.3
e = 1e-9

isEqual = abs(b - a) < e

print(isEqual)
print(a)
print(b)
print(a==b)