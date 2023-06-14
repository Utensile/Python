res = float(input("Inserire Resistenza: "))
parallel=0
series=0
while res > 0:
    parallel+=(1/res)
    series+=res
    res = float(input("Inserire Resistenza: "))

print("Per le resistenze inserite, la resistenza equivalente in serie equivale a "+str(series)+" mentre quella in parallelo vale "+str(1/parallel))
