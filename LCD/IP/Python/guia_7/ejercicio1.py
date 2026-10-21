# def pertenece (s:list,e:int)->bool:
#     res: bool = e in s
#     return res

def pertenece(s:list,e:int)->bool:
    for i in s:
        if e==i:
            return True

#print(pertenece([1,2,3],1))


def divide_a_todos (s:list,e:int)->bool:
    res = True
    for i in s:
        if i % e == 0:
            return True
        else:
            return False


#print(divide_a_todos([2,4,6],2))


def suma_total (s:list)->int:
    res : int = 0 
    for i in range(len(s)):
        res += s[i]
    return res

#print(suma_total([1,2,3]))


def maximo(s:list)->int:
    m : int = 0
    for i in s:
        if i > m:
            m = i
        else:
            pass
    return m

#print(maximo([1,42,3]))



def minimo(s:list)->int:
    m : int = 0
    for i in s:
        if i < m:
            m = i
        else:
            pass
    return m

#print(minimo([-45,0,3]))



def pos_maximo(s:list)->int:
    if len(s)==0:
        return -1
    else:
        pm: int = 0
        mx: int = maximo(s)
        for i in range(len(s)):
            if s[i]>=mx:
                pm = i
            else:
                pass
        return pm

#print(pos_maximo([2,5,89,0,-1]))


def pos_minimo(s:list)->int:
    if len(s)==0:
        return -1
    else:
        pm: int = 0
        mx: int = minimo(s)
        for i in range(len(s)):
            if s[i]>=mx:
                pm = i
            else:
                pass
        return pm


#print(pos_minimo([2,-1,89,0,-1]))




def ordenados(s:list)->bool:
    res: bool = True
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            res = True and res
        else:
            res = False and res

    return res

#print(ordenados([1,5,3]))

def long_mayorASiete(s:list)->bool:
    res: bool = True
    for i in s:
        if len(i)>7:
            res = True and res
        else:
            res = False and res

    return res


#print(long_mayorASiete(["octagenario","octagenario","octagenario","octagenario"]))


def es_palindroma(s:str)->bool:
    if s == [] or len(s)==1:
        return True
    else:
        res : bool = True
        for i in range(len(s)):
            if s[i]==s[-1-i]:
                res = True and res
            else:
                return False
        return True


#print(es_palindroma("neuquen"))

def iguales_consecutivos(s:list)->bool:
    i: int = 0
    j : int = i +1
    k : int = j +1
    res: bool = True
    while (i < len(s)-2):
        if s[i] == s[j] == s[k]:
            res =  True or res
        else:
            res = False or res 
        i += 1
    return res

#print(iguales_consecutivos([3,3,4]))

#VER LUEGO, ME ABURRI





