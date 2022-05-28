# Decorator - super charges or function

from time import time


def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func


@my_decorator
def hello():
    print('Helloooo')


@my_decorator
def bye():
    print('see ya later')


hello()
bye()


def hello2():
    print('Helloooo 2')


# same as decorator
a = my_decorator(hello2)
a()


###########################################################

def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator2
def hello_programmer(greeting, emoji=":)"):
    print(greeting, emoji)


hello_programmer("Hello Programmer", ":(")

############################################################
# practical approaches of decorator


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5


long_time()
