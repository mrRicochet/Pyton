# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите размер шоколадки n: '))
m = int(input('Введите размер шоколадки m: '))
k = int(input('Введите желаемое количество разломов k: '))

if (n-1)//k or (m-1)//k:
    print(f'Мы можем разломить шоколадку {k} раз(а)')
else:
    print(f'Мы не можем разломить шоколадку {k} раз(а)')