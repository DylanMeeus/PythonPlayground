# Raytracer implementation
import math

class Triple:
    """ Triple class and some operations that make sense on them """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self, other):
        self.a += other.a
        self.b += other.b
        self.c += other.c

    def subtract(self, other):
        self.a -= other.a
        self.b -= other.b
        self.c -= other.c

    def __eq__(self, other):
        return  self.a == other.a and self.b == other.b and self.c == other.c

    def __str__(self):
        return "{" + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + "}"

class Vector3(Triple):
    def __init__(self, a, b, c):
        Triple.__init__(self,a,b,c)

    def scalar_multi(self, scalar):
        scalar = float(scalar)
        self.a *= scalar
        self.b *= scalar
        self.c *= scalar

    def scalar_div(self, scalar):
        scalar = float(scalar)
        self.a /= scalar
        self.b /= scalar
        self.c /= scalar

    def vector_multi(self, vector):
        self.a *= vector.a
        self.b *= vector.b
        self.c *= vector.c

    def cross(self, vector):
        new_a = (self.b * vector.c) - (self.c * vector.b)
        new_b = (-(self.a * vector.c) - (self.c * vector.a))
        new_c = (self.a * vector.b) - (self.b * vector.a)
        self.a = new_a
        self.b = new_b
        self.c = new_c

    def dot(self, vector):
        return float(self.a * vector.a + self.b * vector.b + self.c * vector.c)

    def length(self):
        return math.sqrt(a*a + b*b + c*c)
    
    def get_unit_vector(self):
        """ return the current vectors unit vector representation """
        k = 1.0 / self.length()
        return Vector3(self.a * k, self.b * k, self.c *k)


if __name__ == '__main__':
    a = Vector3(1,2,3)
    b = Vector3(3,2,1)

def test():
#if __name__ == '__main__':
    xs = 200
    ys = 100
    max_rgb = 255
    image_content = "P3"
    image_content += "\n" + str(xs) + " " + str(ys) + "\n"
    image_content += str(max_rgb)
    image_content += "\n"
    y = ys
    while y > 0:
        for x in range(xs):
            # create some colours in range 0-1.0
            _r = x / xs
            _g = y / ys
            _b = 0.2
            # convert to actual rgb
            r = int(_r * max_rgb)
            g = int(_g * max_rgb)
            b = int(_b * max_rgb)
            image_content += str(r) + " " + str(g) + " " + str(b) + "\n"
        y -= 1
    print(image_content)



    


