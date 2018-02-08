# Raytracer implementation

if __name__ == '__main__':
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



    


