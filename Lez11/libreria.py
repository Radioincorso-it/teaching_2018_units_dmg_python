def creaLista(file):
    with open(file) as csvfile: 
        listaCSV = [riga.strip().split(';') for riga in csvfile]
    return(listaCSV)