# Ejercicio 4 (2,25 puntos)
# Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

# problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
#   requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
#   asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
#   asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
#   asegura: { Los valores de res son positivos }
# }

#texto= "hola dios soy yo de nuevo"


def limpia_espacios_multiples(texto):
    texto_res: list[str] = []
    for c in range(len(texto)):
        if c==len(texto)-1:
            texto_res.append(texto[c])
        else:
            if texto[c]==' ' and texto[c+1]==' ':
                pass
            elif texto[c]==' ' and not texto[c+1]!=' ':
                texto_res.append(texto[c])
            else:
                texto_res.append(texto[c])
    return texto_res


def obtiene_palabras(texto)->str:
    palabras: list[list[str]] = []
    palabra: str = ''
    for c in range(len(texto)):
        if texto[c] == ' ':
            if palabra == '':
                pass
            else:
                palabras.append(palabra)
                palabra = ''
        else:
            palabra += texto[c]
    
    #ultima palabra
    palabras.append(palabra)
    return palabras


def palabras_por_vocales(texto:str)->dict[int,int]:
    vocales:list[str] = ["a","e","i","o","u","A","E","I","O","U"]
    #ejemplo: {2:1,1:2,3:1}
    lista_palabras : list[str] = obtiene_palabras(limpia_espacios_multiples(texto))
    dict_vocales: dict[int,int] = {}
    for palabra in lista_palabras:
        if palabra == ' ' or palabra == '':
            pass
        else:
            #print(palabra)
            contador : int = 0
            for letra in palabra:
                if letra in vocales:
                    contador += 1
            if contador in dict_vocales.keys():
                dict_vocales[contador] += 1
            else:
                dict_vocales[contador] = 1
    return dict_vocales



print(palabras_por_vocales(" soy yo de nuevo "))


#print(obtiene_palabras(limpia_espacios_multiples("hola dios, soy yo de  nuevo  ")))

#print(limpia_espacios_multiples("hola dios, soy yo de  nuevo  "))
    




