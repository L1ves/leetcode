def bear_fur(bears):
    if bears[0] == bears[1]:
        return bears[0]
    if 'brown' in bears and 'black' in bears:
        return 'dark brown'
    if 'black' in bears and 'white'in bears:
        return 'grey'
    if 'white' in bears and 'brown' in bears:
        return 'light brown'
    if bears[0] and bears[1] == 'yellow' or 'magenta':
        return 'unknown'