from random import randint

conta = 0
num = randint(1, 90)
Nin=-1

while num!=Nin and conta < 5:
    Nin=int(input("Prova a indovinare? "))
    conta+=1
    if num>Nin:
        print("Maggiore")
    elif num<Nin:
        print("Minore")

if(Nin==num):
    print("Hai indovinato!")
else:
    print("Hai finito i 5 tentativi, il numero era " +str(num))
