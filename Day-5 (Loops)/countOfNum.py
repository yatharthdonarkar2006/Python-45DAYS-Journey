count = 0
num = int(input("Enter a number: "))

while(num > 0):
    rem = num % 10
    count = count + 1
    num = num // 10

print("Number of digits:", count)
