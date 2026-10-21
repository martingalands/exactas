sumaRacionales::Int->Int->Float
sumaRacionales n m | n == 1 = fromIntegral (n)
                    | otherwise = sumaParcial n m + sumaRacionales (n-1) m

sumaParcial::Int->Int->Float
sumaParcial q m | q == 1 = fromIntegral (m)
                | otherwise = sumaParcial (q-1) m + (fromIntegral m)/ (fromIntegral q) ---fromInteger? 