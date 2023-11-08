
print("Distancia en la recta numérica")
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese otro número entero: "))

distancia = num1 - num2
if distancia>0:
    print ("La distancia entre ",num1, "y ",num2, "es: ",distancia)
else:
    print ("La distancia entre ",num1, "y ",num2, "es: ",num2-num1)
    