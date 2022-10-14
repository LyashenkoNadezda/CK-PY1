list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
last_num = list_numbers[-1]

max_index = 0

for i, curr_num in enumerate(list_numbers):
    max_num = list_numbers[max_index]
    curr_num = list_numbers[i]
    if curr_num > max_num:
        max_index = i
list_numbers[-1] = list_numbers[max_index]
list_numbers[max_index] = last_num

'''
Второй вариант:
max_num_ind = list_numbers.index(max(list_numbers))
list_numbers[-1] = list_numbers[max_num_ind]
list_numbers[max_num_ind] = last_num
'''

print(list_numbers)
