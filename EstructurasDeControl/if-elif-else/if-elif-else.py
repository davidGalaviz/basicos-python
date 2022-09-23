#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = float(input("Ingresa un número: "))

if num < 0: 
    result = "El número es negativo"
elif num > 0:
    result = "El número es positivo"
else:
    result = "El número es cero"

print(result)

