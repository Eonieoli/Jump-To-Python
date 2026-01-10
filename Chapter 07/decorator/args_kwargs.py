def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, name='foo', age=3)
# func(name='foo', age=3, 1, 2, 3)    # SyntaxError: positional argument follows keyword argument