def add(*numbers):
    sum_of_numbers = 0
    for i in numbers:
        sum_of_numbers += i
    return sum_of_numbers


def print_dict(number, **kwargs):
    print(kwargs)


print(add(5, 4, 6, 7, 3, 8))
print_dict(23, Meet=21, Vishal=27, Bhumika=30)
