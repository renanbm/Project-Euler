sum = 0

for x in range(1, 1001):
    sum += x**x

print(str(sum)[len(str(sum))-10:])
