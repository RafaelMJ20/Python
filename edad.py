#!/cd/Document/Programa
# -*- coding: utf-8 -*-
import os,sys

#################################
#Fecha: 19-10-2021              #
#Autor: Rafael Miranda Jimenez  #
#################################

fecha_Nacimiento = int(input("Digite su año de nacimiento: "))
diferencia = (2021 - fecha_Nacimiento) 

if diferencia >= 18:
    print ("El usuario tiene",diferencia ,"es mayor de edad")

else:
    print ("El usuario tiene",diferencia, "es menor de edad")
