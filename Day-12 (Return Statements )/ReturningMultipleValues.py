# Returning Multiple Values

def calculate(a, b):
    return a + b, a - b

diff_val, sum_val = calculate(10, 5)

print(sum_val)
print(diff_val)