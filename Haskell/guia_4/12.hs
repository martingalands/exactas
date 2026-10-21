raizDe2Aprox::Int->Float

raizDe2Aprox n | n == 1 = 2
               | otherwise = 2+(1/raizDe2Aprox (n-1))