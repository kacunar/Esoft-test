import numpy as np
import random
def esoft_function(n,m):
    if(n<2 or m<2):
        print "Los argumentos deben ser mayor a dos"
    else:
        elements = random.sample(range(1,n*m+1),n*m)
        listt =[elements[index : index + n] for index in (n * i for i in range(m))]
        matrix = np.asarray(listt)
        print(matrix)
        evenColumns= matrix[:,1::2]
        print (evenColumns)
        evenColumnsProm= evenColumns.sum() / float(len(evenColumns[0]))
        print (evenColumnsProm)
        n = 0
        for i in range(len(matrix[0])):
            if ((matrix[:,i].sum()) > evenColumnsProm):
                n= n+1
        print 'La cantidad de columnas cuyo total es mayor a ' + str(evenColumnsProm) + ' es: '  + str(n) 
        return n
        
k = esoft_function(10,10) 


