#manejo de IF ELSE
num1=3
num2=8

'''
relacionales (>,<,<=, !=),
aritmeticos (+,-,*,/),
booleanos (or, and)
'''
if num1!=num2:
    if num1>num2:
        #.format es la posicion en la que estan las llaves
        print("El valor de {} es mayor que {}".format(num1,num2))
    else:
        print("El valor de {} es menor que {}".format(num1,num2))
else:
    #Es que pase y no haga nada
    pass
    