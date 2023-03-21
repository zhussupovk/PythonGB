number = int(input())
res = 0
while number:
    res += number % 10
    number //= 10
print(res)
