# -*- coding: utf-8 -*-
import re
import sys

def programa4(RutaXML):
    text = ""
    xml=open(RutaXML,'r')
    if xml.closed:
        return None
    text=xml.read()
    xml.close()
    return text
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa4(entrada)      # ejecutar 
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
