
--1)
pertenece::(Eq t) => t->[t]->Bool

pertenece x [] = False
pertenece x (t:ts) | x  == t = True
                   | otherwise = pertenece x (ts)



--2)

todosIguales::(Eq t)=>[t]->Bool
todosIguales [] = True
todosIguales [t] = True
todosIguales (t:y:ts) | t == y = True && todosIguales (y:ts)
                      | otherwise = False



--3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:y:xs) | x /= y = True && todosDistintos xs
                      | otherwise = False 




--4)
hayRepetidos:: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs == True = True
                    | otherwise = hayRepetidos (xs)


--5)
quitar::(Eq t)=>t ->[t]->[t]
--datos un entero x y una lista xs, elimina la primera aparicion de x en la lista xs (de haberla)
quitar t [] = []
quitar t (x:xs) | (t == x) = xs
                  | otherwise = x:quitar t (xs)  --alternativamente [x]++quitar t (xs)



--6)quitar todos


quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) | pertenece e (x:xs) == True = quitarTodos e (quitar e (x:xs)) 
                     | otherwise = x:xs

--7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | (pertenece x xs == True) = x:eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x:eliminarRepetidos xs


--8)

longitud::[t]->Int

longitud [] = 0
longitud (t:ts) = longitud ts +1


mismosElementos:: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = False
mismosElementos t r = (longitud sinRepT == longitud sinRepR) && (comparaListas sinRepR sinRepT)
                    where sinRepT = eliminarRepetidos (eliminarRepetidos t)
                          sinRepR = eliminarRepetidos (eliminarRepetidos r)


comparaListas::(Eq t) =>[t]->[t]->Bool
comparaListas [] r = True
comparaListas (t:ts) r = (pertenece t r == True)  == comparaListas ts r
                       

--comparo ambas listas luego de quitar repetidos


--9)
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [x] = True
capicua (x:xs) = (x == head (reverse (x:xs))) == capicua (quitaExtremos (x:xs))

quitaExtremos::[t]->[t]
quitaExtremos (x:xs) = reverse (tail (reverse (xs)))

--[1,2,3,4]--->[2,3,4]
--[2,3,4]---reverse-->[4,3,2]-tail-->[3,2]---->reverse [3,2]

--agarro el primer elemento. obtengo el ultimo elemento. son iguales? quito primer elemento y el ultimo. recursiono pasando el siguiente elemento
--hago un "pliegue". comparo primer elemento contra el primer elemento del reverso

