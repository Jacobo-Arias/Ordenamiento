import json
from time import time
from metods import heapSort, bubbleSort

# toma como entrada una función y las listas con 
# los datos
def tiempos(func,listas):
    for i in listas:
        start = time()
        func(listas[i])
        end = time()
        print("El tiempo para {} fue de {:.4f} segundos".format(i,end-start))


if __name__ == "__main__":
        
    with open('listas.json','r') as json_file:
        listas = json.load(json_file)


    print("==================== Heap Sort =======================")
    #Se llama la función tiempos con la función heapSort
    # y las listas como parametros
    tiempos(heapSort,listas)


    print("==================== Bubble Sort =======================")
    
    #Se llama la función tiempos con la función bubblesort
    # y las listas como parametros
    tiempos(bubbleSort,listas)
