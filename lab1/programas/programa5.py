# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4
from programa2 import programa2
from programa1 import programa1


def programa5(RutaPdf,RutaXML):
    resultado=False
    xml = programa4(RutaXML)
    fecha, monto = programa2(RutaPdf)

    # Busco fecha + importe del mismo movimiento
    movimientos = re.findall(
        r'Importe="([^"]+)"\s+Fecha="([^"]+)"',
        xml
    )

    for m_xml, f_xml in movimientos:
        if fecha == f_xml and monto == m_xml:
            resultado= True
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
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
