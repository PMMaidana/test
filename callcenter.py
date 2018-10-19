from test import Llamada

numero = input("Ingrese numero\n")
inicio = int(input("Ingrese hora de inicio\n"))
fin = int(input("Ingrese hora de fin\n"))

llam1 = Llamada(inicio, fin, numero, 10)
if len(numero) > 7:
    if len(numero) == 8:
        llam1.llamada_national()
    elif len(numero) == 13:
            llam1.llamada_interstate()
    else:
            llam1.llamada_international()
