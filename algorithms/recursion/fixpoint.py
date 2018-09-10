""" test of the fixpoint algorithm """

def fib(a, b, out, lim, func):
    if a > lim:
        return out
    c = a + b
    out.append(c)
    return func(b, c, out, lim)


def func(f):
    return lambda *a: f(*a, func(f))

if __name__ == '__main__':
    fib_function = func(fib)
    fibs = fib_function(0,1,[], 100)
    print(fibs)

