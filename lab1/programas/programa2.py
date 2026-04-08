# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa2(RutaFactura):
    
    texto = programa1(RutaFactura)
    fecha = re.search(r"(\d{4})-(\d{2})-(\d{2})", texto)
    monto = re.search(r"DÉBITO BANCARIO:(\s)*(\d)*,(\d{2})", texto, flags=re.IGNORECASE)
    monto = re.search(r"(\d)*,(\d{2})",monto)

    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
