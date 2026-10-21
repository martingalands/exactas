todosPares::Int->Bool
todosPares n | (n < 10) = mod n 2 == 0
             |  otherwise = (mod n 2 == 0) == todosPares (div n 10)
