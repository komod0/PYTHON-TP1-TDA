import time

fileName="files/file_"
n=10000

arrays=[[],[],[],[],[],[],[],[],[],[]]
selectionArrays=[[],[],[],[],[],[],[],[],[],[]]
insertionArrays=[[],[],[],[],[],[],[],[],[],[]]
quickArrays=[[],[],[],[],[],[],[],[],[],[]]
heapArrays=[[],[],[],[],[],[],[],[],[],[]]
mergeArrays=[[],[],[],[],[],[],[],[],[],[]]

c=0
while 10 > c:
    print("ARCHIVO N°",c)
    file = open(fileName+str(c)+".txt")

    #carga de arrays desde archivos
    i=1
    while n > i:
        line=file.readline()
        i+=1
        x=int(line.strip())
        arrays[c].append(x)

    #copia de arrays
    selectionArrays[c] = arrays[c]
    insertionArrays[c] = arrays[c]
    quickArrays[c] = arrays[c]
    heapArrays [c] = arrays[c]
    mergeArrays[c] = arrays[c]

    #selection sort
    start_time = time.time()
    #selectionSort(selectionArrays[c])
    totalTime = time.time() - start_time
    print("\tEL TIEMPO DE SELECTION ES:", totalTime)

    #insertion sort
    start_time = time.time()
    #insertionSort(selectionArrays[c])
    totalTime = time.time() - start_time
    print("\tEL TIEMPO DE INSERTION ES:", totalTime)

    #heap sort
    start_time = time.time()
    #heapSort(selectionArrays[c])
    totalTime = time.time() - start_time
    print("\tEL TIEMPO DE HEAP ES:", totalTime)

    #merge sort
    start_time = time.time()
    #mergeSort(selectionArrays[c])
    totalTime = time.time() - start_time
    print("\tEL TIEMPO DE MERGE ES:", totalTime)

    #heap sort
    start_time = time.time()
    #selectionSort(selectionArrays[c])
    totalTime = time.time() - start_time
    print("\tEL TIEMPO DE SELECTION ES:", totalTime)


    print("")
    c+=1


