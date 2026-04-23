# -*- coding: utf-8 -*-
import re
import sys
from programa1 import programa1

def programa3(RutaFactura):
    texto = programa1(RutaFactura)
    res = ""
    inicio = re.search(
        r"CANT\w*.*?TOTAL",
        texto,
        re.IGNORECASE | re.DOTALL
    )
    """Busco desde cant hasta total ignorando mayusculas y saltos de linea"""
    if inicio:
        tabla = texto[inicio.end():]
    else:
        tabla = ""
    """"Busco las cosas con formato cant,desc,... """
    items = re.finditer(
        r"^\s*(\d{1,3})\s+(.*?)\s+(\d+,\d{2})\s+(\d+,\d{2})\s*$",
        tabla,
        re.MULTILINE
    )
    for match in items:
        cant = match.group(1)
        desc = match.group(2).strip()
        puni = match.group(3)
        total = match.group(4)

        res += f"Cant: {cant} |Desc: {desc} | {puni} c/u |Total:  {total}\n"

    return res
    
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    with open(salida, 'w', encoding='utf-8') as f:  # abrir archivo salida
        f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
