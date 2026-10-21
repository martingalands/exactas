-- a ":" se le dice cons.

--1:[2,3] = [1,2,3]
--head [1,2,3] = 1
--tail [1,2,3] = [2,3]

ejempplo:

longitud::[a]->Int

longitud [] = 0
longitud (x:xs) = 1+longitud xs

