# 5. Multiplication Table

# Print the multiplication table of a given number up to 10.

num = (int(input("Enter the Table : ")))
i = 0
for i in range(1, 11):
    print(i * num)
    i += i
