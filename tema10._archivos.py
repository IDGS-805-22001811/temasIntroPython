#Crea archivos de texto
from io import open

texto="Una linea con texto\notra linea de texto"
#Siempre que se abra cerrarlo
fichero=open('fichero.txt','w')
fichero.write(texto)

cadena2="\nEsto es otra cadena"
fichero.write(cadena2)

cadena3="\nEsto es otra cadena"
fichero.write(cadena3)
#Aqui se cierra
fichero.close
