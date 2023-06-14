import random as rd

k=0
probability =  [0]*10

for i in range(10000000):
    rand=rd.randint(1, 10)
    probability[rand-1]+=1
    k+=1

final= ""
for i in range(10):
    final+= str(i+1)+": "+str(probability[i]*100/k)+"% | "

print(final)