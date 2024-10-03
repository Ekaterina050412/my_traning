numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_primes = 0
    for j in numbers:
        if i % j == 0:
            is_primes += 1
            if is_primes > 2:
                break
        if i / j < 1:
            break
    if is_primes == 2:
        primes.append(i)
    if is_primes > 2:
        not_primes.append(i)
print(primes)
print(not_primes)
