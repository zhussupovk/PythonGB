number = int(input())
firstThreeDigits = number // 100000 + number // 10000 % 10 + number // 1000 % 10
lastThreeDigits = number % 10 + number % 100 // 10 + number % 1000 // 100
if firstThreeDigits == lastThreeDigits:
    print("Yes!")
else:
    print("No((")
