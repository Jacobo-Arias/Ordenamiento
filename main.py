import json
from time import time
from metods import heapSort, bubbleSort, countingSort

# toma como entrada una función y las listas con 
# los datos
def tiempos(func,listas):
    for i in listas:
        start = time()
        func(listas[i])
        end = time()
        salida = "El tiempo para {} fue de {:.4f} segundos".format(i,end-start)
        with open('salida.txt','a') as file:
            file.writelines(salida+'\n')
        print(salida)


if __name__ == "__main__":
        
    with open('listas.json','r') as json_file:
        listas = json.load(json_file)
    
    k500 = listas.pop('1M')
    listas['500k'] = k500[0:500000]

    with open('salida.txt','w') as file:
        file.writelines("==================== Counting Sort =======================\n")
    print("==================== Counting Sort =======================")
    #Se llama la función tiempos con la función heapSort
    # y las listas como parametros
    tiempos(countingSort,listas)

    with open('salida.txt','a') as file:
        file.writelines("==================== Heap Sort =======================\n")
    print("==================== Heap Sort =======================")
    #Se llama la función tiempos con la función heapSort
    # y las listas como parametros
    tiempos(heapSort,listas)


    with open('salida.txt','a') as file:
        file.write("==================== Bubble Sort =======================\n")
    print("==================== Bubble Sort =======================")
    
    #Se llama la función tiempos con la función bubblesort
    # y las listas como parametros
    tiempos(bubbleSort,listas)
