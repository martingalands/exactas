sacarBlancosRepetidos::[Char]->[Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [c] = [c]
sacarBlancosRepetidos (c:v:cs) | c == ' ' && v == ' ' = sacarBlancosRepetidos (v:cs)
                               | c == ' ' && not (v == ' ') = c:v:sacarBlancosRepetidos cs 
                               | not (c == ' ') && not (v== ' ') = c:v:sacarBlancosRepetidos cs
                               | not (c == ' ') && (v == ' ') = c:sacarBlancosRepetidos (v:cs)



contarPalabras::[Char]->Integer
contarPalabras [] = 0
contarPalabras (x:y:xs) = cuentaBlancos (sacarBlancosRepetidos (reverse (sacarBlancoBorde (reverse (sacarBlancoBorde  (x:y:xs))))))+1


sacarBlancoBorde::[Char]->[Char]
sacarBlancoBorde (x:xs) | (x == ' ') == True = (xs)
                        | otherwise = (x:xs)


cuentaBlancos::[Char]->Integer
cuentaBlancos [] = 0
cuentaBlancos (x:xs) | (x == ' ') == True = 1 + cuentaBlancos (xs)
                     | otherwise = cuentaBlancos xs

--quito los espacios repetidos
--las palabras se delimitan por espacio



