#design combiner
#Designed by Hafidh
from math import *
ro = 130  # base circle radius
X = 40  # triangle fun base


#Square creator
def square(side, color="none",stroke="none"):
    return rectangle(h=side, w=side, fill=color,stroke="none", x=0, y=0)

#centercircle
def circle_pair():
    ccircle = circle(r=45, y=0, fill="  #AB2722", stroke="none")
    ccircle += circle(r=40, y=0, fill="  #D5273E", stroke="none")
    ccircle += circle(r=35, y=0, fill="  #F76150", stroke="none")
    ccircle += circle(r=30, y=0, fill="  #FF8F7D", stroke="none")
    ccircle += circle(r=25, y=0, fill="  #FEC4B9", stroke="none")
    ccircle += circle(r=20, y=0, fill="  #FFE2DA", stroke="none")
    return ccircle | scale(1.3)

#inner triangles


def inner_triangle():
    X = 100
    p1 = [point(x=-X/3, y=X), point(x=X/3, y=X), point(x=0, y=0)]+[point(x=0,y=0), point(x=-X/3, y=-X), point(x=X/3, y=-X), point(-100/3, 100)]
    c = (polyline(p1, fill="#FFE2DA", stroke="none") | scale(.4))+(polyline(p1, fill="#FEC4B9", stroke="none") | scale(.35)) \
        + (polyline(p1, fill=" #FF8F7D", stroke="none") | scale(.30)) + (polyline(p1, fill="#F76150", stroke="none") | scale(.25)) \
        + (polyline(p1, fill="#D5273E", stroke="none") | scale(.20)) + \
        (polyline(p1, fill="#AB2722", stroke="none") | scale(.15))
    return (c+(c | rotate(90)) | rotate(45)) | rotate(23) | scale(1.3)

#Triangle fun
#colourfull triangle
def triangle_pyramid():
    pc1 = "#B31B1B"
    pc2 = "#FFDB49"
    pc3 = "#FF8C00"
    pc4 = "#1F472A"
    p1 = [point(x=-X/2, y=0), point(x=X/2, y=0), point(x=0, y=X-0.1)]
    p2 = [point(x=-X/2, y=0), point(x=X/2, y=0), point(x=0, y=-X+0.1)]
    p3 = [point(x=-X/2, y=0), point(x=X/2, y=0), point(x=0, y=X/3)]

    po1 = (polyline(p1, fill=pc1, stroke=pc1) | scale(.1)) +\
        (polyline(p2, fill=pc1, stroke=pc1) | scale(.1))

    po2 = (polyline(p1, fill=pc2, stroke=pc2) | scale(.15)) +\
        (polyline(p2, fill=pc2, stroke=pc2) | scale(.15))

    po3 = (polyline(p1, fill=pc3, stroke=pc3) | scale(.15)) +\
        (polyline(p2, fill=pc3, stroke=pc3) | scale(.15))

    po4 = (polyline(p1, fill=pc4, stroke=pc4) | scale(.15)) +\
        (polyline(p2, fill=pc4, stroke=pc4) | scale(.15))

    po5 = (polyline(p1, fill="black", stroke="black", stroke_width=2) | scale(.15))

    # polyline(p3,fill="yellow",stroke="black")
    trianglefun = (po1 | translate(0, y=X-3)) +\
        (po2 | translate(-2, X-8))+(po2 | translate(2, X-8)) +\
        (po3 | translate(-4, X-12))+(po3 | translate(0, X-12))+(po3 | translate(4, X-12)) +\
        (po4 | translate(-6, X-16))+(po4 | translate(-2, X-16))+(po4 | translate(2, X-16))+(po4 | translate(6, X-16)) +\
        (po5 | translate(-9, X-22))+(po5 | translate(-5, X-22))+(po5 | translate(-1, X-22)) +\
        (po5 | translate(3, X-22)) + \
        (po5 | translate(7, X-22))+(po5 | translate(9, X-22))
    return trianglefun|scale(1.3)


def circle_groups():
    #side_circles
    subcircle = circle(r=35, y=57, fill="  #c7d2f0", stroke="none")
    subcircle += circle(r=25, y=57, fill=" #483d9c", stroke="none")
    subcircle += circle(r=15, y=57, fill="  #0f1d53", stroke="none")
    subcircle += circle(r=5, y=57, fill="  #110b1f", stroke="none")

    subCircle2 = subcircle | translate(y=-114)
    Combine = subcircle+subCircle2
    Combine2 = Combine | rotate(90)
    GC = Combine+Combine2 | scale(.76)
    GC += GC | rotate(45)
    return GC | scale(1.4)

#square design
def square_spiral():
    red_layer = square(side=180, color='#',stroke="none") | repeat(10,  rotate(10))
    orange_layer = square(side=165, color='#ff9626',stroke="none") | rotate(5) | repeat(10,  rotate(10))
    dark_yellow_layer = square(side=155, color='#ffc23d',stroke="none") | repeat(10,  rotate(10))
    pale_yellow = square(side=145, color='#e7d986',stroke="none") | rotate(5) | repeat(10,  rotate(10))
    white_layer = square(side=135, color='#fcefb1',stroke="none") | repeat(10,  rotate(10))
    g = combine([red_layer, orange_layer, dark_yellow_layer,pale_yellow, white_layer])
    return g


def basics():
    side = 2*ro/sqrt(2)
    outer_circle = circle(x=0, y=100, r=30,fill="#E8502B") | repeat(36, rotate(10))

    inner_square1 = (square(side, color="#070616") | rotate(45)) + \
        circle(r=side/2, fill="#94031e")
    inner_square2 = (square(side, color="#070616"))

    return outer_circle+inner_square1+inner_square2


#colourfull triangle
tf = (triangle_pyramid() | rotate(-45) | translate(x=13, y=13) |scale(1.09)) | repeat(8, rotate(45)) | rotate(22.47) | scale(1.3)

#black stroke circle
c1 = circle(r=(ro/2)-8, stroke="black", stroke_width=9)

#Centre
# cc = (circle(r=10, fill="#45287e", stroke="none") +circle(r=5, fill=" #745d9d", stroke="none")) | scale(1.5)
cc1 = ellipse(h=8, w=3, x=0, y=10, fill="#FFFDE3", stroke="#E6CA73",stroke_width=1) | repeat(150, rotate(100))
cc2 = circle(r=5, fill="yellow", stroke="none")
cc=cc1+cc2
#Screen BG
screen = square(side=350,color="yellow")

#Driver code
if __name__ == "__main__":
    #layerorder
    layer_order = combine([basics(), square_spiral(), circle_groups(), circle_pair(), c1, inner_triangle(), cc])
    show(screen, layer_order, tf)
