ordenar::[Int]->[Int]

--ordenar [] = []
-- ordenar (x:y:xs) | x>=y = x:ordenar (y:xs)
--                  | otherwise = ordenar (y:x:xs)

-- ordenar (x:y:xs) | x >= y = y:ordenar (x:xs)
--                  | otherwise = x:y:ordenar xs


--agarro x, comparo con y. veo cual es el maximo. voy mandando el maximo de a uno al final

maximo [x] = x --caso no recursivo. caso base.
maximo (x:y:xs) | x>y = maximo (x:xs)
                | otherwise = maximo (y:xs)

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


