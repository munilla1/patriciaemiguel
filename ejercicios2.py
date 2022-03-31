
print ("------------ejercicio numero 12:-------------")

numero_a_calcular = 5633 % 2

if numero_a_calcular == 0:
    print("true")
else:
    print("false")




print ("------------ejercicio numero 13:-------------")

edad_del_comprador = 12
articulos_comprados = 2
if edad_del_comprador >= 18:
    print("mayor de 18: True")
else:
    print("mayor de 18: False")
if articulos_comprados >= 1:
    print("compra mayor de 1 articulo: True")
else:
    print("compra mayor de 1 articulo: False")



print ("------------ejercicio numero 15:-------------")

primera_palabra = "complejidad"
segunda_palabra = "algoritmo"

if primera_palabra >= segunda_palabra:
    print("False")
else:
    print("True")




print ("------------ejercicio numero 16:-------------")

print("¿como se llama?")
nombre = input()
print(f'me alegro de conocerle {nombre}')
print("¿y su amigo?")
nombre_2 = input()
print(f'su nombre es, {nombre_2}')

if (nombre[0:0:]) == (nombre_2[0:0:]):
    print(True)
else:
    print(False)




print ("------------ejercicio numero 18:-------------")

print("escribe un numero: ")
numero = input()
print("otro")
numero_2 = input()
print("el mayor de los dos es: ")
if numero > numero_2:
    print(numero)
else:
    print(numero_2)