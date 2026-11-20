# problema ejercicio1 (in s: seq⟨Z⟩) : Z x Z {
#   requiere: { Existen al menos dos posiciones i < j en rango tales que s[i] > s[j] }
#   asegura: { s[res0] > s[res1] }
#   asegura: { res0 < res1 }
#   asegura: { Sean i y j (con i < j) dos posiciones cualesquiera de s tales que s[i] > s[j], entonces res1 - res0 >= j - i }
# }


#agarro el primer elemento y comparo con el segundo. si s[i] > s[j] entonces guardo i y guardo j como (i,j). esto debe estar inicializado en (0,0)
#agarro el primer elemento y comparo con el tercero. si s[i] > s[i] y la distancia es mayor que lo que ya tengo, entonces guardo y piso la variable


#cuando cambio de i, hago lo mismo.

def ejercicio1(s:list[int])->tuple[int,int]:

    res: tuple[int,int] = (0,0)
    for i in range(len(s)):
        for j in range(i,len(s)):
            
            if s[i]>s[j]:
                distancia_actual = j-i
                if distancia_actual >= res[1]-res[0]:
                    res = (i,j)
    return res



print(ejercicio1([0,5,5,2,3,6]))
print(ejercicio1([3,4,2,23,1]))
print(ejercicio1([6,5,4,3,2,1]))
print(ejercicio1([-2,5,4,3,2,1]))
