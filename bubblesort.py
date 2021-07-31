import random
import time
start_time = time.time()

def BubbleSort(lista):
    troca = True
    passnum = len(lista)-1
    while passnum > 0 and troca:
        troca = False
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                troca = True
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
        passnum = passnum-1

lista= random.sample(range(0, 500), 100)
print("LISTA DESORDENADA:",lista)
BubbleSort(lista)
print("LISTA ORDENADA:",lista)
end_time= time.time()
tempo= end_time - start_time
print("tempo de execução:", tempo)