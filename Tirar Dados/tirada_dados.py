# -*- coding: utf-8 -*-
import random
import time

print("¿Desea tirar los dados? S - Sí   N - No")                               

iniciador = True     

a = input()                                                         

while iniciador == True :
    if a == "S" or a == "s" :                                       
        b = int((random.random() * 10) % 6 + 1)
        c = int((random.random() * 10) % 6 + 1)
        print("Los dados marcaron los números:",b,"y",c)
        print("La suma de estos números es:", b + c)
        print("¿Desea volver a tirar los dados? S - Sí   N - No")
        a = input()
    elif a == "N" or a == "n" :                                     
        print("No se tirarán los dados. Que tenga buen día!")       
        iniciador = False                                           
        time.sleep(3)                                               
    else :
        print("No se detectó una entrada válida.")                  
        print("¿Desea volver a tirar los dados? S - Sí   N - No")   
        a = input()

