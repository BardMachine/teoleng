# -*- coding: utf-8 -*-
import re
import sys

from programa1 import leerPdf

def programa3(RutaFactura):
    try:
        text = leerPdf(RutaFactura)
    except Exception as e:
        print(f"No se pudo leer el PDF. ({e})")
        return ""
    
    patron = re.compile(r"^([0-9]+)[ ]+(.+?)[ ]+([0-9]+,[0-9]+)[ ]+([0-9]+,[0-9]+)[ ]+", flags= re.MULTILINE | re.IGNORECASE)
    encuentros = patron.findall(text)

    res = ""
    for m in encuentros:
        res += f"Cant: {m[0]} |Desc: {m[1]} | {m[2]} c/u |Total:  {m[3]}\n"
    
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
