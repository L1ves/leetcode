def nb_year(p0, percent, aug, p):
    # your code
    counter = p0
    year = 0
    new_year_grow = 0
    while True:
        new_year_grow =  int(counter + ((counter * percent) / 100)  + aug)
        year += 1
        counter = new_year_grow
        if counter >= p:
            break
    return counter