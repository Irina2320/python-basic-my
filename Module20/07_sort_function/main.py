def tpl_sort(*args):
    for num in args:
        if type(num) == float:
            return tuple(args)
    else:
        return tuple(sorted(args))




# print(tpl_sort(6, 3, -1, 8, 4, 10.0, -5))
