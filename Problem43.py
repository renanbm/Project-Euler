import itertools

pandigital_list = ["".join(perm) for perm in itertools.permutations("0123456789")]
sum = 0

for pandigital in pandigital_list:
    if (int(pandigital[1] + pandigital[2] + pandigital[3]) % 2 == 0 and
        int(pandigital[2] + pandigital[3] + pandigital[4]) % 3 == 0 and
        int(pandigital[3] + pandigital[4] + pandigital[5]) % 5 == 0 and
        int(pandigital[4] + pandigital[5] + pandigital[6]) % 7 == 0 and
        int(pandigital[5] + pandigital[6] + pandigital[7]) % 11 == 0 and
        int(pandigital[6] + pandigital[7] + pandigital[8]) % 13 == 0 and
        int(pandigital[7] + pandigital[8] + pandigital[9]) % 17 == 0):
        sum += int(pandigital)

print(sum)
