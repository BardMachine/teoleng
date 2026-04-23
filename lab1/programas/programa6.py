# -*- coding: utf-8 -*-
import re
import sys

from programa2 import programa2
from programa4 import leerXML

def programa6(RutaPdf,RutaXML):
    fecha, monto = programa2(RutaPdf)
    if fecha == None:
        return None
    if monto == None:
        return None


    xml = leerXML(RutaXML)
    patron = re.compile(r"^.*?Importe=\"(.+?)\" Fecha=\"([0-9]+-[0-9]+-[0-9]+)\".*?$", flags = re.MULTILINE)
    encuentros = patron.finditer(xml)

    # no encontro ningun movimiento en el xml
    if not encuentros:
        return (False)

    coincidencias = 0

    text = xml
    for m in encuentros:
        if fecha == m.group(2) and monto == m.group(1):
            coincidencias += 1
            text = text[:m.start() - 1] + text[m.end():] # el - 1 es para borrar el newline
            
    
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
