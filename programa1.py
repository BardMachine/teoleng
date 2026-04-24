# -*- coding: utf-8 -*-
import re
import sys

from pypdf import PdfReader

def leerPdf(ruta):
    text = ""
    lector = PdfReader(ruta)
    for pagina in lector.pages:
        text += pagina.extract_text()
    lector.close()
    return text

def programa1(RutaPdf):
    try:
        return leerPdf(RutaPdf)
    except Exception as e:
        print(f"No se pudo leer el PDF. ({e})")
        # Devuelve un string vacio para que no de problemas al llamar progrma1
        return ""

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
