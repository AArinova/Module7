def add_everything_up(aa, bb):

    """сложение числа (int, float) и строки(str)"""
    res = 0
    try:
        res = aa + bb
    except TypeError:
        res = str(aa) + str(bb)
    finally:
        if isinstance( res, float):
            res = round( res, 3)
        return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))