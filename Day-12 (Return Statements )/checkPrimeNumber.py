def prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return count == 2

num = int(input("Enter the Number: "))

if prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")