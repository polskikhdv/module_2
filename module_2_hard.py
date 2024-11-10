import random

rock_1 = random.choice(range(3, 21))
result = []
for a in range(1, rock_1):
    for b in range(1, rock_1):
        if rock_1 % (a + b) == 0 and a < b:
            result.append([str(a), str(b)])
print(f'Первый камень выпал: {rock_1}, пароль к выходу: {''.join(sum(result, []))}')

