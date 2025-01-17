#listas

lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes", "Martes", "Miercoles"]
lista4=["Josue",45,1.92]

print(type(lista1))
print(len(lista1))
print(lista1[0])

x=0
suma=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("La suma es: {}".format(suma)) 
print(lista1)
print(lista1[0])
#Agrega un elemento a la lista
lista1.append(100)
print(lista1)
print(lista1[3])

lista5=[]

for x in range(5):
    valor=int(input("Ingresa un valor: "))
    lista5.append(valor)

print(lista5)    

#eliminar elementos de lista
print(lista1)
lista1.pop()
print(lista1)

'''
Crear prpgrama que pida una cantidad n de numeros y almacenarlos en un arreglo la salida debera ser la siguiente:
Lista completa: xxxxxxx
Numeros pares de la lista: aaaaa
Numeros Impares de la lisfa: rrrrr
'''

lista6 = []  
for i in range(3):
    valor = int(input("Ingresa numero: "))
    lista6.append(valor)

pares = []
impares = []

for numero in lista6:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista:", lista6)
print("Numeros pares:", pares)
print("Numeros impares:", impares)


'''
'''
lista1.sort()#prdenar lista
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)

