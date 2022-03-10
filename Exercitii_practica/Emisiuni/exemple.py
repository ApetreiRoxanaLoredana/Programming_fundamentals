def nr_prime(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        if l[0] < 2:
            return 0
        if l[0] == 2:
            return 1
        if l[0] % 2 == 0:
            return 0
        for d in range(3, l[0] // 2 + 1, 2):
            if l[0] % d == 0:
                return 0
        return 1
    m = len(l) // 2
    return nr_prime(l[m:]) + nr_prime(l[:m])

print(nr_prime([1, 2, 3, 4, 11, 0, -1, 11]))