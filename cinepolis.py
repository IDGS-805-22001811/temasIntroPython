from io import open 
import os

class Cine:
    def __init__(self):
        self.registros = []

    def calcular_descuento(self, boletos_comprados):
        if boletos_comprados > 7:
            return 0.15
        elif 3 <= boletos_comprados <= 5:
            return 0.10
        else:
            return 0

    def calcular_total(self, boletos_comprados, tarjeta):
        precio = 12.000
        descuento = self.calcular_descuento(boletos_comprados)
        sin_descuento = boletos_comprados * precio
        con_descuento = sin_descuento * descuento
        total = sin_descuento - con_descuento
        if tarjeta == 'si':
            total = sin_descuento-(total* 0.10)
        return total

    def historial(self, nombre, total):
        with open('historial.txt', 'a') as fichero:
            fichero.write("Nombre: {}, Total pagado: ${}\n".format(nombre, total))

    def limpiar(self):
        if os.path.exists('historial.txt'):
            with open('historial.txt', 'w') as fichero:
                fichero.write("")  

    def registrar_compra(self, nombre, total):
        self.registros.append((nombre, total))

    def mostrar_registros(self):
        print("Compras realizadas:")
        for nombre, total in self.registros:
            print("Nombre: {}, Total: ${}".format(nombre, total))

    def ejecutar(self):  
        while True:
            nombre = input("Ingresa tu nombre: ")
            compradores = int(input("¿Cuántos compradores son?: "))
            max_boletos = compradores * 7 
            while True:
                total_boletos = int(input("¿Cuántos boletos en total desean comprar?: "))
                if total_boletos > max_boletos:
                    print("Has excedido el límite permitido intentalo nuevamente.")
                else:
                    break
            tarjeta = input("Desea utilizar la tarjeta Cineco? (si/no): ").lower()
            total = self.calcular_total(total_boletos, tarjeta)
            print("Total a pagar: ${}".format(total))
            self.historial(nombre, total)
            self.registrar_compra(nombre, total)
            opcion = input("¿Deseas realizar otra compra? (si/no): ").lower()
            if opcion != 'si':
                self.limpiar() 
                break

        self.mostrar_registros()

cine = Cine()
cine.ejecutar()
