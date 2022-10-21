import random


def get_unique_list_numbers():
    list_ = [random.randint(-10, 10)]
    rng = 15
    count = 1

    while count in range(rng):
        r_num = random.randint(-10, 10)
        if r_num not in list_:
            list_.append(r_num)
            count += 1
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
