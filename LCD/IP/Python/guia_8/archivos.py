from typing import TextIO

def contar_lineas(nombre_archivo:str)->int:
    archivo: TextIO = open(nombre_archivo)
    lineas: list[str] 
    lineas = archivo.readlines()
    cant_lineas: int = len(lineas)
    archivo.close()
    return cant_lineas

#print(open('prueba.txt').readlines())
#print(contar_lineas('prueba.txt'))


#if primer_caracter_de_linea == '#'
def clonar_sin_comentarios(nombre_archivo_entrada:str,nombre_archivo_salida:str):
    archivo_entrada: TextIO = open(nombre_archivo_entrada,'r')
    archivo_salida: TextIO = open(nombre_archivo_salida,'w')
    lista_lineas: list[str] = archivo_entrada.readlines()
    for linea in lista_lineas:
        primer_caracter: str = linea[0][0]
        if primer_caracter == '#':
            pass
        else:
            archivo_salida.write(linea)
    archivo_salida.close()
    archivo_entrada.close()
    return archivo_salida


clonar_sin_comentarios('prueba.txt','salida.txt')