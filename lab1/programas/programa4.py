# -*- coding: utf-8 -*-
import re
import sys

def leerXML(ruta):
    text = ""
    xml = open(ruta, "r")
    if xml.closed:
        return None
    text = xml.read()
    xml.close()
    return text

def programa4(RutaXML):
    return leerXML(RutaXML)
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa4(entrada)      # ejecutar 
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
