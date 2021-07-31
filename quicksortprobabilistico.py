import random
import time

start_time = time.time()

def quicksort(lista, inicio, fim):
    if (inicio < fim):
        pivoindex = particionarandomico(lista,inicio, fim)
        quicksort(lista, inicio, pivoindex - 1)
        quicksort(lista, pivoindex + 1, fim)

#função que define o pivô randômico
def particionarandomico(lista, inicio, fim):
    randpivo = random.randrange(inicio, fim)
    lista[inicio], lista[randpivo] = lista[randpivo], lista[inicio]
    return particionamento(lista, inicio, fim)

def particionamento(lista, inicio, fim):
    pivo = inicio
    i = inicio + 1
    for j in range(inicio + 1, fim + 1):
        if lista[j] <= lista[pivo]:
            lista[i], lista[j] = lista[j], lista[i]
            i = i + 1
            lista[pivo], lista[i - 1] = lista[i - 1], lista[pivo]

    pivo = i - 1
    return (pivo)

if __name__ == "__main__":
    lista = random.sample(range(0, 500), 100)
    print("LISTA DESORDENADA:",lista)
    quicksort(lista, 0, len(lista) - 1)
    print("LISTA ORDENADA:",lista)
    end_time= time.time()
    tempo = end_time - start_time
    print("tempo de execução", tempo)
