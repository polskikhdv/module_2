numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    for j in numbers[1:i]:
        if i % j == 0:
            not_primes.append(i)
            break
        else:
            primes.append(i)
            break
print(primes)
print(not_primes)
