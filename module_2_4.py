numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    is_prime = True
    for j in numbers[1:i]:
        if i % j == 0:
            if j == i:
                is_prime = True
            else:
                is_prime = False
        else:
            break
    if is_prime == True:
        primes.append(i)
    else: not_primes.append(i)
print(primes)
print(not_primes)
