# -*- coding: utf-8 -*-
import re
import sys

from programa2 import programa2
from programa4 import leerXML

def programa6(RutaPdf,RutaXML):
    # este carga un pdf y me da la fecha y el monto
    fecha, monto = programa2(RutaPdf)
    if fecha == None:
        return ""
    if monto == None:
        return ""

    try:
        xml = leerXML(RutaXML)
    except Exception as e:
        print(f"No se pudo leer el XML. ({e})")
        return ""

    patron = re.compile(r"^.*?Importe=\"(.+?)\" Fecha=\"([0-9]+-[0-9]+-[0-9]+)\".*?$", flags = re.MULTILINE | re.IGNORECASE)

    coincidencias = 0

    # esta es una solucion alternativa si hubiese que sustituir mas de una linea.
    """
    text = xml
    encuentro = True
    while encuentro == True:
        encuentro = False
        encontrados = patron.finditer(text)
        for m in encontrados:
            if fecha == m.group(2) and monto == m.group(1):
                encuentro = True
                coincidencias += 1
                text = text[:m.start() - 1] + text[m.end():] # el - 1 es para borrar el newline
                break
    """
    # solucion final. (sustituye una sola linea)
    text = xml
    encontrados = patron.finditer(text)
    for m in encontrados:
        if fecha == m.group(2) and monto == m.group(1):
            coincidencias += 1
            text = text[:m.start() - 1] + text[m.end():] # el - 1 es para borrar el newline
            break
    
    patron_mov = re.compile(r"<BanTeng:TotalMovimientos>([0-9]+)</BanTeng:TotalMovimientos>", flags = re.MULTILINE)
    m = patron_mov.search(text)
    coincidencias = int(m.group(1)) - coincidencias
    text = patron_mov.sub(f"<BanTeng:TotalMovimientos>{coincidencias}</BanTeng:TotalMovimientos>", text)

    return text

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
