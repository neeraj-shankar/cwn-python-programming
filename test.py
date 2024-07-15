def my_decorator(*args, **kwargs):
    print(args)
    print(len(args))
    print(callable(args))


my_decorator(42, debug=True)