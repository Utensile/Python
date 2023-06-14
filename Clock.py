import g2d
from math import pi, sin, cos

g2d.init_canvas((500, 500))
g2d.set_color((50, 52, 63))

for i in range(60):
    angle = i * (2*pi / 60)
    pt1 = 250 + 210*cos(angle), 250 + 210*sin(angle)
    pt2 = 250 + 250*cos(angle), 250 + 250*sin(angle)
    g2d.draw_line(pt1, pt2)

g2d.main_loop()
