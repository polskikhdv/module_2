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


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Список чисел, которые будем проверять
# Создадим два пустых списка для хранения простых и не простых чисел
primes = []
not_primes = []
# Проходим по каждому числу в нашем списке
for number in numbers:
    # Пропускаем число 1, так как оно не является ни простым, ни составным
    if number == 1:
        continue
    # Предполагаем, что число простое
    is_prime = True
    # Проверяем делимость числа на все числа от 2 до числа (исключая само число)
    for i in range(2, number):
        # Если нашли делитель, то число не простое
        if number % i == 0:
            is_prime = False
            break
    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим результат
print("Простые числа:", primes)
print("Непростые числа:", not_primes)