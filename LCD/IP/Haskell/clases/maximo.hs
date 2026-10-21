--dada una secuencia de enteros devuelve un entero

maximo::[Int]->Int

maximo [x] = x --caso no recursivo. caso base.
maximo (x:y:xs) | x>y = maximo (x:xs)
                | otherwise = maximo (y:xs)
            


--OPCION 2
maximo::[Int]->Int

maximo [x] = x --caso no recursivo. caso base.
maximo (x:xs) | max x (maximo xs)

max::Int->Int
max x y | x>y = x
        | otherwise = y

                