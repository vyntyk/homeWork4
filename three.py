# 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in -1 out Negative value of the number of numbers! []
#  in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

userList = list(map(int, input('Введите числа списка через пробел: ').split()))
print(f'Ваш список: {userList}')

uniqueList = []

for i in range(len(userList)):
    for j in range(len(userList)):
        if i != j and userList[i] == userList[j]:
            break
    else:
        uniqueList.append(userList[i])



print(f'Cписок неповторяющихся элементов {uniqueList} вашего списка!')

