def eliminate_unset_bits(number):
    # TODO
    if "1" in number:
        return int(''.join(number.split('0')),2)
    else:
        return int(0)