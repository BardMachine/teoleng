# -*- coding: utf-8 -*-
import re
import sys
from programa4 import programa4
from programa2 import programa2
from programa1 import programa1
from programa5 import programa5

def programa6(RutaPdf,RutaXML):
    text = ""
    xml = programa4(RutaXML)
    fecha, monto = programa2(RutaPdf)
    patron = r'<BanTeng:Movimiento[^>]*Importe="' + monto + r'"[^>]*Fecha="' + fecha + r'"[^>]*/>\s*\n?'
    if not re.search(patron, xml):
        return xml

    xml = re.sub(patron, '', xml, count=1)
    match_total = re.search(r'<BanTeng:TotalMovimientos>(\d+)</BanTeng:TotalMovimientos>', xml)
    
    if match_total:
        total = int(match_total.group(1))
        totaln = total - 1

        text = re.sub(
            r'<BanTeng:TotalMovimientos>\d+</BanTeng:TotalMovimientos>',
            '<BanTeng:TotalMovimientos>' + str(totaln) + '</BanTeng:TotalMovimientos>',
            xml
        )

    return text
 

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
