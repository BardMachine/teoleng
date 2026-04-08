# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa2(RutaFactura):
    
    texto = programa1(RutaFactura)
    fecha_rev = re.search(r"(\d{2})-(\d{2})-(\d{4})", texto)
    costo = re.search(r"DÉBITO(\s)*BANCARIO(\s)*(\d)*,(\d{2})", texto, flags=re.IGNORECASE)
    if costo and fecha_rev:
        fecha_rev = fecha_rev.group()
        fecha = ""
        fecha = fecha_rev[6:10] + "-" + fecha_rev[3:5] + "-" + fecha_rev[0:2]
        monto = re.search(r"(\d)*,(\d{2})",costo.group())
        monto = monto.group()
        return fecha, monto
    else:
        return "",""
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
