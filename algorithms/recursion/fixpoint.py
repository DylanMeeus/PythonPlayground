""" test of the fixpoint algorithm """

# recurisive
def fib(a, b, out, lim, func):
    if a > lim:
        return out
    c = a + b
    out.append(c)
    return func(b, c, out, lim)


def func(f):
    """ fixpoint function """
    return lambda a,b,c,d: f(a,b,c,d,func(f))


if __name__ == '__main__':
    fib_function = func(fib)
    fibs = fib_function(0,1,[], 100)
    print(fibs)