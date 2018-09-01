import numpy as np
from PIL import Image
from numba import jit


@jit
def in_mandlebrot(c, iters=256) -> 'Int' :
    z = c
    for i in range(iters):
        if abs(z) > 2:
            return i
        z = z*z + c
    return 0

def get_colour(iters: int) -> '(int,int,int)':
    """ get a colour based on the iterations it took to determine if a number was inside the set """
    if iters == 0: # the number is in the set
        return (0,0,0)
    else:
        r = int(0.5 * iters)
        g = int(0.5 * iters)
        b = int(0.5 * iters)
        return (r,g,b)

def generate_mandlebrot(x_range: int, y_range: int, width: int, height: int) -> 'None':
    xs = np.linspace(x_range[0], x_range[1], width)
    ys = np.linspace(y_range[0], y_range[1], height)
    mandlebrot = [] # array containing the colours / pixels
    for y in range(height):
        for x in range(width):
            # make a complex value out of the xs/ys
            c = complex(xs[x], ys[y])
            value = in_mandlebrot(c)
            mandlebrot.append(get_colour(value))
    im = Image.new('RGB', (width, height))
    im.putdata(mandlebrot)
    im.save("mybrot.png")

if __name__ == '__main__':
    width = 400
    height = 400
    x_range = (-2, 0.5)
    y_range = (-1.25, 1.25)
    generate_mandlebrot(x_range, y_range, width, height)



    
