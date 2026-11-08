def mantuvieron_residencia(censo1:dict[str,str],censo2:dict[str,str])->dict[str,int]:
    res : dict[str] = {}
    for clave in censo1.keys():
        partido: int = censo1[clave]
        if partido == censo2[clave]:
            if not partido in res.keys():
                res[partido] = 1
            else:
                res[partido] += 1
        
    return res



print(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Merlo', 'Ana': 'Merlo'}))