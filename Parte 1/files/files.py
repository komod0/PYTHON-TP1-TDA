import random

a=0
b=1000
n=10000
fileName = "archivo_10.txt"

random.seed(10)
file = open(fileName,"w")

i=0

while n > i:
    randNumber =random.randint(a, b)
    file.write(str(randNumber)+'\r\n')
    i+=1

file.close()