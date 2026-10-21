mayorDigitoPar::Int->Int
mayorDigitoPar n = avanzoComparo n (-1)  -- <----candidato -1 por si las moscas. si no encuentra ninguno entonces da -1

avanzoComparo::Int->Int->Int
avanzoComparo n candidato   | (div n 10 < 10) && (esPar && (indiceActual > candidato)) = indiceActual
                            | (div n 10 < 10) && (esPar && not (indiceActual > candidato)) = candidato
                            | (div n 10 < 10) && (not esPar) = candidato
                            | esPar && (indiceActual > candidato) = avanzoComparo (div n 10) indiceActual
                            | (not esPar) || (esPar && not (indiceActual > candidato)) = avanzoComparo (div n 10) candidato
                            
                            where indiceActual = mod n 10
                                  esPar = mod indiceActual 2 == 0


--separar en casos is the way


--agarro el primero (mod n 10). es par? si--> es el mayor (por ahora)-->guardo-->quito ese numero y aumento indice (div n 10)
--                          no --> aumento indice (div n 10)
--agarro el segundo (mod n 10). es par? si---> es mayor que candidato? --> si---> piso la variable candidato.
--                           si---> es mayor que candidato? --> no---> div n 10
--                           no---> div n 10
--div n 10 < 10?--->si. es par? si---> es mayor que candidato? ---->si. entonces ese es el mayor digito par. devuelvo candidato
--              --->no. sigo la logica anterior.
--              --->si. es par? no--->vale el ultimo candidato.
--              --->si. es par? si---> es mayor que candidato?----->no. entonces vale el ultimo candidato.

