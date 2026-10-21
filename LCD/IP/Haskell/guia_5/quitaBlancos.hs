sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [' '] = [' ']
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | ((x == ' ') && (y == ' ')) == True = x:sacarBlancosRepetidos (xs)
                               | otherwise = x:y:sacarBlancosRepetidos (xs)



contarPalabras :: [Char] -> Integer
contarPalabras (x:y:xs) = cuentaBlancos (reverse (sacarBlancoBorde (reverse (sacarBlancoBorde (sacarBlancosRepetidos (x:y:xs))))))


sacarBlancoBorde::[Char]->[Char]
sacarBlancoBorde (x:xs) | (x == ' ') == True = (xs)
                        | otherwise = (x:xs)


cuentaBlancos::[Char]->Integer
cuentaBlancos (x:xs) | (x == ' ') == True = 1 + cuentaBlancos (xs)
                     | otherwise = cuentaBlancos xs

--quito los espacios repetidos
--las palabras se delimitan por espacio
