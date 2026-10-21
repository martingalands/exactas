module SolucionT2 where

-- Ejercicio 1
f1 :: Integer -> Integer -> Integer

f1 d h | (h == d) = 0
       | esAbundante h == True = 1 + f1 d (h-1)
       | otherwise = f1 d (h-1)


esAbundante::Integer->Bool
esAbundante n = sumaDivisores (divisoresPropios (n)) > n 

divisoresPropios :: Integer ->[Integer]
divisoresPropios n = divideYAgrega n n

divideYAgrega::Integer->Integer->[Integer]
divideYAgrega n 1 = [1]
divideYAgrega n d | n == d = divideYAgrega n (d-1)
                  | mod n d == 0 = d:divideYAgrega n (d-1)
                  | otherwise = divideYAgrega n (d-1)

sumaDivisores [] = 0
sumaDivisores (x:xs) = x+sumaDivisores (xs)




-- Ejercicio 2
f2 :: [(String, Integer, Integer)] -> [String]
f2 [] = []
f2 (cur:curs) = miraCursada (cur)++f2 (curs)

miraCursada::(String, Integer, Integer)->[String]
miraCursada (nombreCurs,a,c) | ((a <= 2021) && (c >= 1)) || (a < 2021) = [nombreCurs]
                             | otherwise = []




-- Ejercicio 3
f3 :: [Integer] -> Integer -> [Integer]

f3 [] u = []
f3 (s:ss) u | s<0 = []
            | (0 <= s) && (s <= u) = s:f3 ss u
            | s > u = u:f3 ss u




-- Ejercicio 4
f4 :: [[Integer]] -> Integer -> Integer
f4 [] _ = 0
f4 (fila:filas) col = cuentaPares fila 0 col + f4 filas col 

cuentaPares::[Integer]->Integer->Integer->Integer
cuentaPares [] _ _ = 0
cuentaPares (elem:elems) cont col | (mod elem 2 == 0) && (cont == col-1) = 1 + cuentaPares elems (cont+1) col
                                  | otherwise = cuentaPares elems (cont+1) col




