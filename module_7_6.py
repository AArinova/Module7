def add_everything_up(aa, bb):

    """сложение числа (int, float) и строки(str)"""
    res = 0
    try:
        res = round(aa + bb, 3)
    except TypeError:
        res = str(aa) + str(bb)
    finally:
        return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))