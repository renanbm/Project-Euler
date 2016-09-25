def dec_to_bin(x):
    return int(bin(x)[2:])


def palindromic(x):
    x_str = str(x)
    for i in range(len(x_str)):
        if x_str[i] != x_str[len(x_str) - 1 - i]:
            return False
    return True

answer = 0

for x in range(1000000):
    if palindromic(x) and palindromic(dec_to_bin(x)):
        answer += x

print(answer)
