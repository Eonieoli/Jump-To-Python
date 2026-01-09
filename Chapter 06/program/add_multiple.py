def add_multiple(num1, num2):
    total = 0
    for i in range(1000):
        if i % num1 == 0 | i % num2 == 0:
            total += i
    return total

print(add_multiple(3, 5))