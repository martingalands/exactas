--esto es como un for. hago tantas veces la recursion como cantidad de digitos que
--tengo que avanzar.
--tengo iesimoDigito 5745 3:
--tengo 4 digitos. hago 3 veces div 10

iesimoDigito::Int->Int->Int
iesimoDigito n i = mod (div n (10^(cantDigitos (n)-i))) 10


cantDigitos::Int->Int
cantDigitos 0 = 1
cantDigitos n | div n 10 == 0 = 1
              | otherwise = cantDigitos (div n 10) + 1