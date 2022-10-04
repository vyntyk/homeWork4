# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа in 54 out [2, 3, 3, 3] in 9990 out [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]


N = int(input("Введите натуральное число N: "))

def Multiplier(y):
    list = []
    x = 2
    while x * x <= y:
        if y % x == 0:
            list.append(x)
            y //= x
        else:
            x += 1
    if y > 1:
        list.append(y)
    return list

print(f"Список простых множителей числа {N} равен: ")
print(Multiplier(N))
