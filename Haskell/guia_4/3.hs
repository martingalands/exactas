esDivisible::Int->Int->Bool
dividir::Int->Int->Int->Bool

--esto es parecido a un while

esDivisible m n | m >= n = dividir m n (n-1)
                | otherwise = False


dividir m n c | m == n*c = True
              | (m > n*c) = dividir m n (c+1)
              | otherwise = False

--m = n*c +r
--m = dividendo
--n = divisor 
--c = cociente
--r = resto

--tenia dos parametros. precisaba una variable. como esDivisible toma dos parametros
--necesité una funcion mas para poder hacer "R3->Bool". hago el llamado a otra funcion
--y ejecuto la recursion en "dividir".
