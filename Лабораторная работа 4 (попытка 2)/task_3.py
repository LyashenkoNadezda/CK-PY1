def delete(list_, index=None):
    if index is None:
        res = list_[:-1]
    else:
        if index == 0:
            res = list_[index + 1:]
        else:
            res = list_[:index] + list_[index + 1:]
    return res


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))


'''
Прошлое решение:

def delete(list_, index=None):
    if index is None:
        del list_[-1]
    else:
        res = list_[:index] + list_[index:]
    return res


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
'''
