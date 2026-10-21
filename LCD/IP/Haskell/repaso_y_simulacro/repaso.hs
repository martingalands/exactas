-- generarStock :: [String] ->[(String, Int)]
-- generarStock [] ()

-- cuentaProducto 

divisoresPropios :: Int ->[Int]

divisoresPropios n = divideYAgrega n n

divideYAgrega::Int->Int->[Int]
--d:divisor
divideYAgrega n 1 = [1]
divideYAgrega n d | mod n d == 0 = d:divideYAgrega n (d-1)
                  | otherwise = divideYAgrega n (d-1)



sonAmigos :: Int ->Int ->Bool
sonAmigos n m = sumaDivisores (divisoresPropios n) == sumaDivisores (divisoresPropios m)

sumaDivisores::[Int]->Int
sumaDivisores [] = 0
sumaDivisores (x:xs) = x+sumaDivisores (xs)



--[["hola","hola"],["hola","hola"]] = ["holahola","holahola"]
