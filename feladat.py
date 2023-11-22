import random
import math
def prim(x:int):
    if x <=1:
        print("Nem primszam")
    elif x==2:
        print("A 2 primszam")
    else:
        i:int=2
        oszto_db: int=0
        while i < x-1 and (x%i!=0):

            oszto_db+=1
            i+=1
        if i==x-1:
            print(f"{x} prim")
        else:
            print(f"{x} nem prim")

def feladatveletlen():
    list=[]
    vszam:int=0
    i:int=0
    while i < 5:
        szam=math.floor(random.random(36-10)+10)
        list.append()
