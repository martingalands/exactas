#res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j) 

#cantidad_parejas_que_suman (in s: seq⟨Z⟩, in n: Z) : Z

def cantidad_parejas_que_suman(s:list[int], n:int)->int:
    pareja: list[int] = []
    cuenta:int = 0
    i:int = 0
    while i <= len(s)-1:
        long_restante: int = len(s)-i-1
        j:int = i+1
        while j+i <= long_restante:
            if s[i]+s[j]==n:
                cuenta += 1
            #print(j)
            j += 1
        i += 1
    return cuenta
        
#print(cantidad_parejas_que_suman([1,1], 2))
