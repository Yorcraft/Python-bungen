import random
x1 = random.randint(1, 10)
x2 = random.randint(1, 10)
x3 = random.randint(1, 10)
x4 = random.randint(1, 10)
x5 = random.randint(1, 10)
x6 = random.randint(1, 10)
x7 = random.randint(1, 10)
numbers = [x1, x2, x3, x3, x5, x6, x7, x1, x2, x3, x3, x5, x6, x7]
for number in numbers:
    out = ""
    for printx in range(number):
        out += "*"
    print(out)

numbers = [3, 5, 6, 7, 1, 9, 18]


for max in numbers:
    for x in numbers:
        if x > max:
            max = x
print(max)