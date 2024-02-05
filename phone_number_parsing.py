def create_phone_number(n):
    #your code here
    #s = ''.join(str(x) for x in n)
    s = ''.join(map(str,n))
    return f'({s[0:3]}) {s[3:6]}-{s[6:11]}'

#best practice
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)