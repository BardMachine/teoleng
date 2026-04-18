# -*- coding: utf-8 -*-
import re
import sys

from pypdf import PdfReader

def leerPdf(ruta):
    lector = PdfReader(ruta)
    if lector == None:
        return None
    if lector.get_num_pages() == 0:
        lector.close()
        return None
    text = lector.pages[0].extract_text()
    for i in range(1, len(lector.pages)):
        text += '\n' + lector.pages[i].extract_text()
    lector.close()
    return text

def programa1(RutaPdf):
    return leerPdf(RutaPdf)


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
