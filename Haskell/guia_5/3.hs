--1)
sumatoria::[Int]->Int
sumatoria [] = 0
sumatoria (x:y:xs) = x+y+sumatoria xs


--2)
productoria::[Int]->Int
productoria [] = 1
productoria (x:xs) = x*productoria xs


--dada una secuencia de enteros devuelve un entero

---3)

maximo::[Int]->Int
maximo [x] = x
maximo (x:xs) | x>=maximo xs = x
              | otherwise = maximo xs
            



--4)
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (x+n):sumarN n (xs)


--5)
--sumarElPrimero :: [Int] -> [Int]
--sumarElPrimero (x:y:xs) = [2*x]++sumaPrimero x (y:xs)

--sumaPrimero::Int->[Int]->[Int]
--sumaPrimero x [] = []
--sumaPrimero x (y:ys) = [x+y]++sumaPrimero x (ys)


--6)
sumarElUltimo::[Integer] -> [Integer]
sumarElUltimo (x:ys) = reverse (sumarElPrimero (reverse (x:ys)))

sumaPrimero::Integer->[Integer]->[Integer]
sumaPrimero x [] = []
sumaPrimero x (y:ys) = [x+y]++sumaPrimero x (ys)


sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:y:xs) = [2*x]++sumaPrimero x (y:xs)


--7)
pares:: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x:pares (xs)
             | otherwise = pares xs

--8)
multiplosDeN::Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x:multiplosDeN n (xs)
                      | otherwise = multiplosDeN n (xs)



--9)
ordenar::[Int]->[Int]

--ordenar [] = []
-- ordenar (x:y:xs) | x>=y = x:ordenar (y:xs)
--                  | otherwise = ordenar (y:x:xs)

-- ordenar (x:y:xs) | x >= y = y:ordenar (x:xs)
--                  | otherwise = x:y:ordenar xs


--agarro x, comparo con y. veo cual es el maximo. voy mandando el maximo de a uno al final

-- maximo [x] = x --caso no recursivo. caso base.
-- maximo (x:y:xs) | x>y = maximo (x:xs)
--                 | otherwise = maximo (y:xs)

--HECHO EN CLASE
ordenar [] = []
ordenar (x:xs) = ordenar ( quitar (maximo (x:xs)) (x:xs))++[maximo (x:xs)]

quitar t [] = []
quitar t (x:xs) | (t == x) = xs
                  | otherwise = x:quitar t (xs)  --alternativamente [x]++quitar t (xs)

--VERSION SIMPLIFICADA
--ordenar ys = ordenar(quitar(maximo ys)) ++ [maximo ys]


--MAS SIMPLIFICADA AUN
--ordenar ys = ordenar (quitar m ys) ++[m]
--where m = maximo ys


