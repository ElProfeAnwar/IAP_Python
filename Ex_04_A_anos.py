print("EX_4_A_Comparador de años")
anio1 = int(input("Ingrese un año: "))
anio2 = int(input("Ingrese otro año: "))

diferencia = anio1-anio2

if anio1 > anio2 and diferencia == 1 :
    print("Ha pasado un año.")
elif anio1 > anio2 :
    print("Han pasado ", diferencia, " años")  
elif anio1 < anio2:
    diferencia = anio2-anio1
    print("Faltan ", diferencia, " años")
else:
    print("Son iguales")


