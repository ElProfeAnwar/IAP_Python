print("Años Bisiestos")
anio = int(input("Ingrese el año a procesar: "))
if (anio % 4)!=0:
    print("El Año no es bisiesto")
else:    
    if (anio %100==0) and (anio %400!=0):
        print("No bis: Mult. de 100 pero no de 400")
    elif (anio %100==0) and (anio %400==0):
        print("Bis: Mult. de 100 y de 400") 
    else :
        print("Es bisiesto")
        
        
        
        
    
    
    
    
    
