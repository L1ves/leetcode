def return_array_not_negative(a_list):
    if not a_list:
        raise ValueError("Input list cannot be empty.")
    zero_index = 0
    odd_elements = []
    for index, n in enumerate(a_list):
        if n % 2 == 0:
            a_list[zero_index] = n
            zero_index += 1
        else:
            odd_elements.append(n)
    a_list[zero_index:] = odd_elements
    return a_list


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
return_array_not_negative(a_list)