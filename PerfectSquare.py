import math

num=int(input("Inserisci il numero: "))
k=math.sqrt(num)
if(k-round(k,0)==0):
    print("Il numero è il quadrato perfetto di "+ str(k))
else:
    print("Il numero non è un quadrato perfetto")
