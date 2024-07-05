lst = '3 4 5 2 3 4 5 6 1 2 8'
my_lst = [int(i) for i in lst.split()]
lst1 = [i for i in my_lst if my_lst.count(i) == 1]
print(*lst1)

#2
st1 = list(map(int, lst.strip().split()))
lst1 = [i for i in lst if lst.count(i) == 1]
print(*lst1)