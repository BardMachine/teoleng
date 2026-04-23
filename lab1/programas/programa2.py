# -*- coding: utf-8 -*-
import re
import sys

from programa1 import leerPdf

def programa2(RutaFactura):
    text = leerPdf(RutaFactura)
    if text == None:
        return None, None
    
    m = re.search(r"(FECHA:)[ \n\r]*([0-9]+)[-/]([0-9]+)[-/]([0-9]+)", text, flags=re.MULTILINE)
    if m == None:
        return None, None

    fecha = f"{m.group(4)}-{m.group(3)}-{m.group(2)}"

    m = re.search(r"(D[ÉE]BITO[ \n\r]*BANCARIO)[ \n\r]*([0-9]+),([0-9]+)", text, flags=re.MULTILINE)
    if m == None:
        return fecha, None

    monto = m.group(2) + "," + m.group(3)

    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w', encoding='utf-8')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida