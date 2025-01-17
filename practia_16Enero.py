#Calcular la distancia entre 2 puntos, pedir cuales seran esos dos puntos, y cuales son la distancia entre esos dos
#Usar la formula
import math
def calcular_distancia(x1, y1, x2, y2):
  distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return distancia

print("Dame las coordenadas del primer punto:")
x1 = float(input("Coordenada x: "))
y1 = float(input("Coordenada y: "))

print("Dame las coordenadas del segundo punto:")
x2 = float(input("Coordenada x: "))
y2 = float(input("Coordenada y: "))

distancia = calcular_distancia(x1, y1, x2, y2)
print("La distancia entre los dos puntos es:", distancia)
