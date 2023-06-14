import g2d
import numpy as np
from random import randint


g2d.init_canvas((1100, 1100))
grid=10

text=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]# A=65, j=74
gameMap=np.zeros((10, 10))
size=np.zeros((10, 10))
flotta=np.zeros((10, 10))
navi=[6, 4, 4, 3, 3, 2, 2, 2, 2]
tiri=0
vittoria=0

def drawBoard():
    global grid
    for i in range(grid+2):
        for j in range(grid+2):
            if(i!=grid and j!=0):
                g2d.set_color((173, 216, 230))
            else:
                g2d.set_color((200, 200, 200))
            g2d.draw_rect((j*1000/grid,i*1000/grid),(1000/grid-1,1000/grid-1))
            g2d.set_color((0, 0, 0))
            if(i==grid and j!=0):
                g2d.draw_text_centered(text[j-2], (j*1000/grid-500/grid,i*1000/grid+500/grid), 20)
            elif(j==0 and i!=grid):
                g2d.draw_text_centered(str(9-i), (j*1000/grid+500/grid,i*1000/grid+500/grid), 20)
    g2d.set_color((120, 120, 120))
    g2d.draw_rect((0,10000/grid),(1000/grid-1,1000/grid-1))
    
def drawCasella(x, y, color):
    x+=1;
    y=9-y
    g2d.set_color(color)
    g2d.draw_rect((x*1000/grid,y*1000/grid),(1000/grid-1,1000/grid-1))

def posiziona_nave(l, nave):
    global flotta
    global gameMap
    global size              
    found=0
    while(not found):
        d=randint(0, 1)
        if(d==0):
            x=randint(0, 9-l)
            y=randint(0, 9)
        else:
            x=randint(0, 9)
            y=randint(0, 9-l) 
        while(gameMap[x][y]!=0):
            d=randint(0, 1)
            if(d==0):
                x=randint(0, 9-l)
                y=randint(0, 9)
            else:
                x=randint(0, 9)
                y=randint(0, 9-l)
        found=1
        for i in range(l):
            if(d==0):
                if(gameMap[x+i][y]!=0):
                    found=0
                    break
            else:
                if(gameMap[x][y+i]!=0):
                    found=0
                    break
    if(found):
        for i in range(l):
            if(d==0):
                gameMap[x+i][y]=1
                size[x+i][y]=l
                flotta[x+i][y]=nave
            else:
                gameMap[x][y+i]=1
                size[x][y+i]=l
                flotta[x][y+i]=nave

def drawNavi():
    for i in range(10):
            for j in range(10):
                if(gameMap[i][j]==1):
                    l=size[i][j]
                    if(l==6):
                        color=(39, 55, 77)
                    elif(l==4):
                        color=(82, 109, 130)
                    elif(l==3):
                        color=(157, 178, 191)
                    elif(l==2):
                        color=(221, 230, 237)
                    drawCasella(i ,j, color)
def drawUpdate(x, y):
    global grid
    global gameMap
    if(gameMap[x][y]==2):
        g2d.set_color((20, 108, 148))
        g2d.draw_text_centered("x",((x+1)*1000/grid+500/grid,(9-y)*1000/grid+500/grid-30) ,1900/grid-1)
    elif(gameMap[x][y]==3):
        if(navi[int(flotta[x][y])-1]>0):
            g2d.set_color((237, 43, 42))
            g2d.draw_circle(((x+1)*1000/grid+500/grid,(9-y)*1000/grid+500/grid), 400/grid-1)
        else:
            for i in range(10):
                for j in range(10):
                    if(flotta[i][j]==flotta[x][y]):
                        l=size[x][y]
                        if(l==6):
                            color=(39, 55, 77)
                        elif(l==4):
                            color=(82, 109, 130)
                        elif(l==3):
                            color=(157, 178, 191)
                        elif(l==2):
                            color=(221, 230, 237)
                        drawCasella(i ,j, color)
                        g2d.set_color((237, 43, 42))
                        g2d.draw_circle(((i+1)*1000/grid+500/grid,(9-j)*1000/grid+500/grid), 400/grid-1)
                        g2d.set_color((210/2, 19/2, 18/2))
                        g2d.draw_text_centered("x",((i+1)*1000/grid+500/grid,(9-j)*1000/grid+500/grid-30) ,1900/grid-1)

def elabora(x, y):
    global tiri
    global flotta
    global gameMap
    global size
    global vittoria
    if(gameMap[x][y]==0):
        gameMap[x][y]=2
        g2d.alert("Hai Mancato!")
        tiri-=1
    elif(gameMap[x][y]==2):
        g2d.alert("Hai già provato a colpire quella casella!")
    elif(gameMap[x][y]==1):
        gameMap[x][y]=3
        navi[int(flotta[x][y])-1]-=1
        if(navi[int(flotta[x][y])-1]>0):
            g2d.alert("Hai colpito una nave di dimensione "+str(size[x][y])[0]+ "\n Riottieni il tuo tiro!")
        else:
            g2d.alert("Hai affondato una nave di dimensione "+str(size[x][y])[0]+ "\n Riottieni il tuo tiro e ne guadagni un altro!")
            tiri+=1
            vittoria=1
            for i in range(9):
                if(navi[i]!=0):
                    vittoria=0
                    break
                    
    elif(gameMap[x][y]==3):
        g2d.alert("Hai già colpito la nave che si trovava in quella casella!")
    
def start():
    drawBoard()
    global vittoria
    global tiri
    tiri=int(g2d.prompt("Benvenuto su Battaglia Navale Python by Montecchi Leonardo\nScegli la diffioltà inserendo il massimo numero di tiri:"))
    nave=1
    for i in navi:
        posiziona_nave(i, nave)
        nave+=1
    print(gameMap)
    vittoria=0
    while(tiri>0 and not vittoria):
        pos=g2d.prompt("Hai ancora "+ str(tiri) +" tiri, scegli quale casella colpire(A0-J9):")
        while(len(pos)!=2 or ord(pos[0])<65 or ord(pos[0])>74):
            pos=g2d.prompt("Stringa Invalida! Hai ancora "+ str(tiri) +" tiri, riprova(A0-J9):")
        x=ord(pos[0])-65
        y=int(pos[1])
        elabora(x, y)
        drawUpdate(x, y)
    if(tiri==0):
        g2d.alert("Hai perso! Le navi erano disposte così:")
        drawNavi();
    else:
        g2d.alert("Hai vinto! Congratulazioni, avevi ancora "+ str(tiri) +" tiri rimanenti")


start()

g2d.main_loop()
