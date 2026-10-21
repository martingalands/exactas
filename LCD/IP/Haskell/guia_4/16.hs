--a) 

menorDivisor::Int->Int

menorDivisor n = divide n 1


divide::Int->Int->Int
divide n i | (i == 1) || not (mod n i == 0) = divide n (i+1)
           | (mod n i == 0) = i


--b)
esPrimo::Int->Bool

esPrimo n | ((divide n 1) == n) == True = True
          | otherwise = False


--c) 8 y 4 son coprimos. tienen el 2 como comun divisor
sonCoprimos::Int->Int->Bool
sonCoprimos n m | (divide n 1) == (divide m 1) = True
                | otherwise = False

--d) n = 1 es el numero 2. el primo n = 2 es el numero = 3. el primo numero 5 es el 11
nEsimoPrimo::Int->Int
nEsimoPrimo n = avanzaPrimo n 2 1

--cada vez que encuentra un true, tiene que hacer n-1 y avanzar en el contador de primos y avanzar en probar que 
--el i-esimo entero es primo o no
avanzaPrimo :: Int->Int->Int->Int
avanzaPrimo n i p | n == 0 = p
                  | (esPrimo i == True) = avanzaPrimo (n-1) (i+1) i
                  | (esPrimo i == False) = avanzaPrimo (n) (i+1) i