import g2d

g2d.init_canvas((1000, 1000))
rows = int(input("Righe: "))
cols = int(input("Colonne: "))

blue= 255/cols
green= 255/rows

for i in range(rows):
    for j in range(cols):
        g2d.set_color((0, 255/rows*i, 255/cols*j))
        g2d.draw_rect((j*1000/cols,i*1000/rows),(1000/cols-1,1000/rows-1))

g2d.main_loop()
