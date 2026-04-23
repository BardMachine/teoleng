# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa2(RutaFactura):
    fecha = ""
    monto = ""
    texto = programa1(RutaFactura)
    fecha_rev = re.search(r"\d{2}\s*[-/]\s*\d{2}\s*[-/]\s*\d{4}", texto)
    costo = re.search(r"D[ÉE]BITO\s*BANCARIO\s*([\d.,]+)", texto, flags=re.IGNORECASE)
    if costo and fecha_rev:
        fecha_rev = fecha_rev.group()
        partes = re.split(r"\s*[-/]\s*", fecha_rev)
        fecha = f"{partes[2]}-{partes[1]}-{partes[0]}"
        monto = costo.group(1)
    return fecha, monto
    
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
