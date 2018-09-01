import numpy as np
from PIL import Image
from numba import jit


@jit
def in_mandlebrot(c, iters=256):
    z = c
    for i in range(iters):
        if abs(z) > 2:
            return i
        z = z*z + c
    return 0


if __name__ == '__main__':
    width = 200
    height = 200
    xs = np.linspace(-2, 0.5, width)
    ys = np.linspace(-1.25, 1.25, height)
    mandlebrot = [] # array containing the colours / pixels
    for y in range(height):
        for x in range(width):
            # make a complex value out of the xs/ys
            c = complex(xs[x], ys[y])
            value = in_mandlebrot(c)
            if value == 0:
                mandlebrot.append((0,0,0))
            else:
                mandlebrot.append((255,255,255))
    im = Image.new('RGB', (width, height))
    im.putdata(mandlebrot)
    im.save("mybrot.png")



    
