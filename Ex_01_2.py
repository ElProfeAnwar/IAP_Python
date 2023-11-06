num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
opcion= str(input("Ingrese s para sumar, r restar, m multiplicar, d dividir"))
if opcion =="s" or "S":     
    print ("La suma es: ", num1+num2)
elif opcion =="r" or "R":     
    print ("La diferencia es: ", num1-num2)
elif opcion =="m" or "M":     
    print ("el producto es: ", num1*num2)
elif opcion =="d" or "D":     
    print ("El cuociente es: ", num1/num2)
          