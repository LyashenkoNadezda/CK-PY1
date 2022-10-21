from pprint import pprint

num = 15
dict_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(num + 1)]

pprint(dict_)
