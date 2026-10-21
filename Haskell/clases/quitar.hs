quitar::(Eq t)=>t ->[t]->[t]

--datos un entero x y una lista xs, elimina la primera aparicion de x en la lista xs (de haberla)

quitar t [] = []
quitar t (x:xs) | (t == x) = xs
                  | otherwise = x:quitar t (xs)  --alternativamente [x]++quitar t (xs)





