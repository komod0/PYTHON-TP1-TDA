import random

a=0
b=1000
n=10000
x=10

fileName = "file_"+str(x)+".txt"
random.seed(x)
file = open(fileName,"w")

i=0

while n > i:
    randNumber =random.randint(a, b)
    file.write(str(randNumber)+'\n')
    i+=1

file.close()