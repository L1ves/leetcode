def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    return sorted([x**2 for x in array1]) == sorted(array2)
#variant C
#      quadro = []
#     for i in array1:
#         quadro.append(i*i)
#     sort_quadro = sorted(quadro)
#     sort_array2 = sorted(array2)
#     counter = len(array1)
#     count = 0
#     for x,y in zip(sort_quadro,sort_array2):
#         if y == x:
#             count +=1
#     if count == counter:
#         return True
#     else:
#         return False