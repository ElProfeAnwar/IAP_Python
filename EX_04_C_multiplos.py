
print("EX_04_C Múltiplos")
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese otro número entero: "))
if num1==0 or num2 == 0:
    print("No puede ingresar 0")
elif num1 <0 or num2 < 0:
    print("No puede ingresar negativos")
elif num1>num2:
    if (num1 % num2) ==0:
        print("El número ",num1, " es múltiplo de ", num2)
    else:
        print("No son múltiplos")
elif num1<num2:
    if (num2 % num1) ==0:
        print("El número ",num2, " es múltiplo de ", num1)
    else:
        print("No son múltiplos")
else:
    print("Son iguales")

    
    