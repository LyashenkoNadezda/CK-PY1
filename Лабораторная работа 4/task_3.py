def delete(list_, index=None):
    if index is None:
        del list_[-1]
    else:
        list_.remove(index)
    return list_


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
