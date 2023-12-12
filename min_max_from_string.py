def high_and_low(numbers):
    # ...
    split_int = []
    split_numbers = numbers.split()
    for i in split_numbers:
        split_int.append(int(i))
    numbers = f'{max(split_int)} {min(split_int)}')
    return ''.join(numbers.split(''))

# def high_and_low(numbers):
#     split_numbers = [int(i) for i in numbers.split(" ")]
#     return "%i %i" % (max(split_numbers),min(split_numbers))