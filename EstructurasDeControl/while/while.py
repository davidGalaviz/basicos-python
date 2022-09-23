#!/usr/bin/env python
# coding: utf-8

# In[ ]:


byte = input("Ingresa 7 bits(0 y 1): ")
while byte != "":
    if byte.count("0") + byte.count("1") != 7 or len(byte) != 7:
        print("No insertaste 7 bits")
    else:
        unos = byte.count("1")
        if unos % 2 == 0:
            print("El bit de paridad debe ser 0.")
        else:
            print("El bit de paridad debe ser 1.")
    byte = input("Ingresa 7 bits")

