char_dict = {}
char_perc = {}

def get_count_char(str_):
    for letter in str_.lower():
        if letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


'''
Пункт 5 задания:

def char_percents(dict_):
    num_sum = 0
    for key, value in dict_.items():
        num_sum += value
    for key, value in dict_.items():
        if key in dict_:
            char_perc[key] = str(round(((value / num_sum) * 100), 3)) + ' %'
        else:
            char_perc[key] = str(round((1 / num_sum) * 100, 3)) + ' %'
    return char_perc


print(char_percents(char_dict))
'''
