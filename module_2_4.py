numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
        else:
            break
    if is_prime == True:
        primes.append(i)
    else: not_primes.append(i)
print(primes)
print(not_primes)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print("Простые числа:", primes)
print("Непростые числа:", not_primes)