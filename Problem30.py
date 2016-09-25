sum = -1

for x in range(0, 9**5*6):
    x_str = str(x)
    temp_sum = 0
    for i in x_str:
        temp_sum += int(i)**5
    if temp_sum == x:
        sum += x

print(sum)
