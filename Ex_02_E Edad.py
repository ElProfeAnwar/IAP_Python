print("Este es el año de la edad!")
anio_actual = int(input("Ingrese año actual: "))
anio_nac = int(input("Ingrese año nacimiento: "))
edad = anio_actual-anio_nac
print ("Usted tiene ", edad)
#Con IF ELIF

if edad >= 18 and edad <65:
    print ("Mayor de edad")
elif edad >=65:
    print("Tercera edad")
else:
    print("Menor de edad")

#Con si anidado
""" 
if edad >= 65:
    print("Tay awelito")
else:
    if edad >= 18:
        print("y es mayor de edad")
    else:
        print("Erís terrile pollo")
"""    
