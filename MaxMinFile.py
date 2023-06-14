
maxN="undefined"
minN="undefined"
with open("input.txt") as file:
    for line in file:
        x=float(line)
        if(minN=="undefined"):
            maxN=x
            minN=x
        elif(x>maxN):
            maxN=x
        elif(x<minN):
            minN=x
print("max: " + str(maxN)+ " min: "+ str(minN))
