# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите 3х значное число: '))

a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10
res = a1 + a2 + a3
print(f'Сумма цифр трехзначного числа = {res}')