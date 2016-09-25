def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

sum = -3 # Ignores 1 and 2

for x in range(0, 2540160):
    x_str = str(x)
    temp_sum = 0
    for i in x_str:
        temp_sum += factorial(int(i))
    if temp_sum == x:
        sum += x

print(sum)
