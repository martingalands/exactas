esCapicua::Int->Bool


esCapicua n | n < 10 = True
            | otherwise = ((div n (10^(cantDigitos n-1))) == (mod n 10)) == esCapicua (quitaExtremos (n))


cantDigitos::Int->Int
cantDigitos 0 = 1
cantDigitos n | div n 10 == 0 = 1
              | otherwise = cantDigitos (div n 10) + 1


quitaExtremos::Int->Int
quitaExtremos n = div (n - (div n mult * mult)) 10
                    where mult = 10^(cantDigitos (n)-1)


---cuento la cantidad de digitos.
--por ejemplo, si son 3 digitos, entonces hago:
--mod n 10 == div n 10^(cantDigitos -1) <-----esto es mirar el primer digito y el ultimo digito
--si es True avanzo con el siguiente digito.

-- div n 10^cantDigitos == mod 