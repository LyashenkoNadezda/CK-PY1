from random import sample
import string as s


def get_random_password(length=8) -> str:
    nums_letters = [i for i in (s.digits + s.ascii_letters)]
    password = sample(nums_letters, length)
    str_ps = ''
    for i in password:
        str_ps += str(i)
    return str_ps


n = 20
print(get_random_password(n))
