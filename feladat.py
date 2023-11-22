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
    lista=[]
    vszam:int=0
    i:int=0
    while i < 5:
        vszam=math.floor(random.random()*(35-10)+10)
        lista.append(vszam)
    return lista
szia=feladatveletlen()
def feladatkiir(lista):
    for i in range(0,len(lista),1):
        print(f"A lista {i} eleme: {lista[i]}")
feladatkiir(szia)