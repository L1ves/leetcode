# Задание 3
#
# Напишите программу, которая:
#
# получает на вход строку чисел, разделенных запятыми;
# формирует из чисел два списка – с четными и нечетными числами;
# выводит списки без скобок на отдельных строках.

lst = [int(i) for i in int(input()).split(',')]
odd = [i for i in lst if i % 2 == 0]
even = [i for i in lst if i % 2 != 0]
input = 3,4,2,7,8,9,1,11,2,56,2,6,81
print(*odd, *even)