def insertionSort(lista):
   for indice in range(1,len(lista)):

     valoreCorrente = lista[indice]
     posizione = indice

     while posizione>0 and lista[posizione-1]>valoreCorrente:
         lista[posizione]=lista[posizione-1]
         posizione = posizione-1

     lista[posizione]=valoreCorrente


     
miaLista = [3,29,71,34,8,55,91,5,27]

print(miaLista)
insertionSort(miaLista)
print(miaLista)

