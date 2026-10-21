import GHC.Read (list)
--agarro el primero, sumo el primero con la lista vacia. avanzo.
--agarro el segundo, sumo el segundo con el primero con la lista vacia. avanzo



-----CHAT GPT

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) = x : sumaAux x xs


sumaAux :: (Num t) => t -> [t] -> [t]
sumaAux acumulado [] = []
sumaAux acumulado (x:xs) = (acumulado + x) : sumaAux (acumulado + x) xs



--2)
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = reverse (listaPrimos x x):descomponerEnPrimos xs


listaPrimos :: Integer -> Integer -> [Integer]
listaPrimos n i | n == 1 = []
                | esPrimo i && esDivisor = i:listaPrimos (div n i) i  ------sigo dividiendo al mismo numero. me olvido del n original porque ya inicializó la recursion
                | otherwise = listaPrimos n (i-1)
                where esDivisor = mod n i == 0

--n = 30 ---> 30 no es primo, entonces hago listaPrimos 30 29
--n = 30 ---> 29 es primo, pero no es divisor, entonces hago listaPrimos 30 28
--continuo...
--n = 30 ---> 5 es primo y es divisor----> 5:listaPrimos (div 30 5) 5
--n = 6 ----> 5 no divide al 6---->listaPrimos 6 4
--n = 6 ----> 3 divide al 6 y es primo -----> 3:listaPrimos (div 6 3) 3
--n = 6 ----> 2 divide al 2 y es primo -----> 2:listaPrimos (div 2 2) 2
--n = 1 ----> cae en caso []


divide::Integer->Integer->Integer
divide n i | (i == 1) || not (mod n i == 0) = divide n (i+1)
           | (mod n i == 0) = i


esPrimo::Integer->Bool
esPrimo n | ((divide n 1) == n) == True = True
          | otherwise = False
