module SolucionT2 where

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

f1::Integer->Integer->[Integer]

f1 d h | (h == d) = []
       | esAbundante h == True = h:f1 d (h-1)
       | otherwise = f1 d (h-1)



---------------------------------------

--f2 :: [(String, Integer, Integer)] -> [String]
--[("Algoritmos y Estructuras de Datos I", 2020, 2), ("Algoritmos y Estructuras de Datos II", 2022, 1)] debe devolver ["Algoritmos y Estructuras de Datos I"]

--devuelve todo lo que esta antes que (2022,1). o sea, 2021,

--barreCursada::[(String,Integer,Integer)]

--agarro el primer elemento, miro el año de aprobacion. si el año es mayor o igual a 2021 y el cuatri es mayor o igual a 0, entonces lo apendeo a la lista


f2 :: [(String, Integer, Integer)] -> [String]
f2 [] = []
f2 (cur:curs) = miraCursada (cur)++f2 (curs)

miraCursada::(String, Integer, Integer)->[String]
miraCursada (nombreCurs,a,c) | ((a <= 2021) && (c >= 1)) || (a < 2021) = [nombreCurs]
                             | otherwise = []



-- -- Ejercicio 3
f3 :: [Integer] -> Integer -> [Integer]

f3 [] u = []
f3 (s:ss) u | s<0 = []
            | (0 <= s) && (s <= u) = s:f3 ss u
            | s > u = u:f3 ss u


---append de enteros de s  desde que 
--si s[i] esta entre 0 y u, queda s[i]
--si s[i]>u  entonces queda u

--[3,8,5,0,7,-2,4] 5 debe devolver [3,5,5,0,5]


-- -- Ejercicio 4
-- f4 :: [[Integer]] -> Integer -> Integer
-- f4 _ _ = 0


--[[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 2

f4 :: [[Integer]] -> Integer -> Integer
f4 [] _ = 0
f4 (fila:filas) col = cuentaPares fila 0 col + f4 filas col 

cuentaPares::[Integer]->Integer->Integer->Integer
cuentaPares [] _ _ = 0
cuentaPares (elem:elems) cont col | (mod elem 2 == 0) && (cont == col-1) = 1 + cuentaPares elems (cont+1) col
                                  | otherwise = cuentaPares elems (cont+1) col



