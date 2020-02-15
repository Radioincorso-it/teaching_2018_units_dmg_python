def creaListaCSV(file):
    f = open(file) 
    listaCSV=[]
    for riga in f:
        s = riga.strip().split(';')
        listaCSV.append(s)
    return(listaCSV)
