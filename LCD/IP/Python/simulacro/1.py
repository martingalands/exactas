
# Ejercicio 1


def ejercicio1(s: list[int], n: int) -> list[int]:
    #barro toda la lista intentando sumar con una subsecuencia el valor n.
    #si hay varias subsecuencias que logran eso, entonces me quedo  con la ultima
    #intento sumar numeros de la lista hasta sumar n.
    
    res:list[int] = []
    for i in range(len(s)):
        suma_parcial: int = 0
        #j:int = i
        res_candidata : list[int] = []
        # while suma_parcial <= n:
        #     suma_parcial += s[j]
        #     res_candidata.append(s[j])
        #     j += 1
        for j in range(i,len(s)):
            if suma_parcial == n:
                res: list[int] = res_candidata
            else:
                suma_parcial += s[j]
                res_candidata.append(s[j])
    return res

print(ejercicio1([1,3,2,5,4,1,2], 5))





# res_candidata: list[int] = []
#     suma_parcial: int = 0
#     for i in range(len(s)):
#         if suma_parcial < n:
#             res_candidata.append(s[i])
#             suma_parcial += s[i]
#             i += 1
#         elif res_candidata == n:
            



    
    