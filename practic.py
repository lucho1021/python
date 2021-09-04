#puntoA

"""factorial = input ('ingresa un numero ')

factorial = int (factorial)

def calculafactorial(factorial):

    if factorial==0 or factorial==1:
            resultado=1
    elif factorial > 1:
            resultado=factorial*calculafactorial(factorial-1)
    return resultado


print("el factorial de",factorial ,"es: ",calculafactorial(factorial))"""



# puntoB

"""num = input('ingresa un numero ')

num = int(num)

def calcularFibonacci(num):
    i = 0
    n1 = 0
    n2 = 1
    for i in range(num):
       print(num, end=' ')
       num = (num-1) + (num-2)
    return num

print(calcularFibonacci(num)) """


"""
num = int(input("Ingresa el limite del fibonacci "))



def calcularFibonacci(num):
    n1= 0 
    n2 =  1
    count = 1
#ingresar un numero correcto
    if num <= 0:
        print("Opss ingresaste un numero incorrecto, revisa e intentalo nuevamente")
    else:
        print("secuencia fibonacci: ")
        while count < num:
            print(n1)
            resultadito = n1 + n2
            n1 = n2
            n2 = resultadito
            
    return n1 

    print(calcularFibonacci(num))"""

    #puntoC

"""
prestamo = int(input("Ingresa el valor del prestamo: "))

cuota = int(input("Ingresa el total de cuotas a pagar: "))

def calcularcuotavalor(prestamo, cuota):
    resultadocuota = prestamo / cuota
    tasamensual = resultadocuota * 0.03
    resultadoT = resultadocuota + tasamensual
    return resultadoT

print("El total a pagar cada cuota es de: ",calcularcuotavalor(prestamo,cuota))"""

    #puntoD

"""
mostrardatos = ["hola", "asd", 13]

print(mostrardatos)"""

    #puntoE

"""
diccionario = {"saludo": "hola", "pregunta": "¿?"}
print (diccionario["saludo"])"""

    #puntoF

"""
dpagos = {"placa": "tis123", "marca": "Aveo", "pagos":[100,200,30,400]}

print (sum(dpagos["pagos"]))"""

    #punto4

"""
datos = int(input("Ingresa la cantidad de datos a ingresar: "))
i = 1

while i <= datos:
    print(i)
    i += 1 """

    #punto5
"""
datosimp = int(input("Ingresa la cantidad de datos a ingresar: "))
i = 1

while i <= datosimp:
    print(i)
    i += 1 * 2   """

datos3 = int(input("Ingresa la cantidad de datos a ingresar: "))
i = 3

while i <= datos3:
    print(i)
    i += 1 * 10
