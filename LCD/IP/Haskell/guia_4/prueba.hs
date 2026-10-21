todosPares::Int->Bool

todosPares n | (not mod (mod n 10) 2 == 0) = False
             | otherwise = todosPares (div n 10)

                
cantDigitos::Int->Int
cantDigitos 0 = 1
cantDigitos n | div n 10 == 0 = 1
              | otherwise = cantDigitos (div n 10) + 1