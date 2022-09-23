#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = float(input("Ingresa un número: "))

if num > 0:
    adjetivo = " "
    if num >= 1000:
        adjetivo = "muy grande"
    elif num >= 100:
        adjetivo = "grande"
    result = "Es realmente un número " + adjetivo + " y positivo" 

elif num < 0:
    result = "El número es negativo"
else:
    result = "El número es cero"

print(result)

