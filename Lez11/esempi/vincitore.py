def creaListaCSV(file):
    f = open(file) 
    listaCSV=[]
    for riga in f:
        s = riga.strip().split(';')
        listaCSV.append(s)
    return(listaCSV)

def winners(f_in):
    l_partite = creaListaCSV(f_in) 
    nomi = l_partite[0]
    print(nomi)
    vincite=[]
    for i in range(len(nomi)):
            vincite.append(0) 
    for riga in range(1,len(l_partite)):
        for col in range(len(l_partite[1])):
            l_partite[riga][col]=int(l_partite[riga][col])
        if min(l_partite[riga])!= max(l_partite[riga]):
            for col in range(len(l_partite[1])):
                if l_partite[riga][col] == max(l_partite[riga]):
                    vincite[col]+=1 
    print('Vincite:',vincite)  
    winners =""
    for i in range(len(nomi)):
        if vincite[i]==max(vincite):
            winners=winners+nomi[i]+ " "
    return(winners)
