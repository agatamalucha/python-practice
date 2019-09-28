def square(a):
    return a**2

type (square)

def cube(a):
    return a**3

def select_function(fn_n):
    if fn_n==1:
        return square
    else:
        return cube


def exec_funtion(fn, n):
    return fn(n)

exec_funtion(cube,3)

