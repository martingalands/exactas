fib::Int->Int

fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)



--13 es fibonacci.
--la cuenta comienza en cero. si se pasa de n entonces el numero no es fibonacci.
--si es igual en algun punto, entonces lo es.


esFibonacci :: Int -> Bool
esFibonacci n = barreFibonacci n 0

barreFibonacci::Int->Int->Bool
barreFibonacci n i | n < fib i = False
                   | otherwise = (fib i == n) || barreFibonacci n (i+1)

