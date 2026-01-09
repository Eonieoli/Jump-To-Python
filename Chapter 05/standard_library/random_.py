import random

print(random.random())

print(random.randint(1, 10))

print(random.randint(1, 55))

data = [1, 2, 3, 4, 5]
print(random.sample(data, len(data)))
print(random.sample(data, 3))