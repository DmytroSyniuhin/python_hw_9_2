def difference(*args):
    if len(args) > 0:
        result_ = round(max(args) - min(args), 2)
    else:
        result_ = 0

    return result_


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
