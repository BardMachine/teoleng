# -*- coding: utf-8 -*-
import re
import sys

from programa2 import programa2
from programa4 import leerXML

def programa5(RutaPdf,RutaXML):
    resultado = False
    
    fecha, monto = programa2(RutaPdf)
    if fecha == None:
        return False
    if monto == None:
        return False

    xml = leerXML(RutaXML)
    patron = re.compile(r"^.*?Importe=\"([0-9]+,[0-9]+)\" Fecha=\"([0-9]+-[0-9]+-[0-9]+)\".*?$", flags = re.MULTILINE)
    encuentros = patron.findall(xml)

    # no encontro ningun movimiento en el xml
    if not encuentros:
        return (False)

    for m in encuentros:
        if fecha == m[1] and monto == m[0]:
            return (True)
    
    if resultado:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
