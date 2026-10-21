

cantidadDeApariciones::Integer->[[Integer]]->Integer
cantidadDeApariciones e [] = 0
cantidadDeApariciones e ((fila:filas)) = barreFila e (fila) + cantidadDeApariciones e (filas)


barreFila::Integer->[Integer]->Integer
barreFila e [] = 0
barreFila e (elem:elems) | e == elem = 1 + barreFila e (elems)
                         | otherwise = barreFila e (elems)



--recorro toda la matriz
--recorro cada lista de la matriz
--uso funcion contador. cada vez que tengo True sumo 1

