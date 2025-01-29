class OperaBas:
    # Declaración de propiedades
    num1 = 0
    num2 = 0
    res = 0

    # Declaración del constructor de la clase
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    # Declaración de los métodos de la clase
    def suma(self):
        self.res = self.num1 + self.num2
        return self.res

def main():
    obj = OperaBas(3, 4)
    resultado = obj.suma()
    print("La suma es:", resultado)

if __name__ == "__main__":
    main()


