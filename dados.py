# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:47:46 2022

@author: victo
"""
import random
num = 0

def tirar_dado():
    num=random.randint(1, 6)
    return num

#codigo para recibir la lanzada de dados del usuario

# funcion que retorna el valor aleatorio
print (tirar_dado())
