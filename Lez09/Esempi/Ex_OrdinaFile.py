def listaSenzaDoppionni(file):
   f=open(file)
   s=f.read();
   sv=s.split()
   risposta=[]
   for c in sv:
      if c not in risposta:
         risposta.append(c)
   risposta.sort()
   return risposta

     
