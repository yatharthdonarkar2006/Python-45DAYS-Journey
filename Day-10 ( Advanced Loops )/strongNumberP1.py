num = int(input("Enter the number : "))

originalNum = num
factSum = 0

while num > 0:

    lastDigit = num % 10

    fact = 1
    for i in range(1, lastDigit + 1):
        fact *= i

    factSum += fact

    num = num // 10

if originalNum == factSum:
    print("It is a Strong Number")
else:
    print("Not a Strong Number")