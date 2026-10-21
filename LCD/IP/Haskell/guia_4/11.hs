--sin fromInteger esto es virtualmente imposible

eAprox :: Int -> Float
eAprox n
    | n == 0    = 0
    | otherwise = 1 / factorial n + eAprox (n - 1)


factorial :: Int -> Float
factorial i
    | i == 0    = 1
    | otherwise = fromIntegral i * factorial (i - 1)


--b)

--no entiendo que hay que hacer.
