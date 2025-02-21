def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__} с аргументами: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")
