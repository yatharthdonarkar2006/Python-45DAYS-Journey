n = int(input("Enter N : "))

for num in range(1, n + 1):

    originalNum = num
    digits = len(str(num))
    armSum = 0

    temp = num

    while temp > 0:
        lastDigit = temp % 10
        armSum += lastDigit ** digits
        temp = temp // 10

    if armSum == originalNum:
        print(originalNum, end=" ")