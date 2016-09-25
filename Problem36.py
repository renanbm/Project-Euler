def dec_to_bin(x):
    return int(bin(x)[2:])


def palindromic(x):
    if str(x) != str(x)[::-1]:
        return False
    return True

answer = 0

for x in range(1000000):
    if palindromic(x) and palindromic(dec_to_bin(x)):
        answer += x

print(answer)
