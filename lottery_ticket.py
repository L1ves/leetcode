#черновик
ticket = [['ABC', 65], ['HGR', 74], ['BYHT', 74]]

ticket_part = ['HGTYREJ', 74]
counter = 0
for i in ticket_part[0]:
    if i == chr(ticket_part[1]):
        counter += 1
