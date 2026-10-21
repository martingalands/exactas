--1)
sumaTotal::[[Integer]]->Integer

sumaTotal [] = 0
sumaTotal (fila:filas) = sumaFila (fila) + sumaTotal (filas)
                       

sumaFila::[Integer]->Integer
sumaFila [] = 0
sumaFila (col:cols) = col + sumaFila cols



--2)

cantidadDeApariciones :: Integer -> [[Integer]] -> Integer 
cantidadDeApariciones e [] = 0
cantidadDeApariciones e (fila:filas) = cuentaEnFila e (fila) + cantidadDeApariciones e (filas)

cuentaEnFila::Integer->[Integer]->Integer
cuentaEnFila e [] = 0 
cuentaEnFila e (col:cols) | col == e = 1 + cuentaEnFila e (cols)
                          | otherwise = cuentaEnFila e (cols)



--3)
contarPalabras::String->[[String]]->Integer
contarPalabras p [] = 0
contarPalabras p (fila:filas) = barreFila p (fila) + contarPalabras p (filas)

barreFila::String->[String]->Integer
barreFila p [] = 0
barreFila p (pal:pals) | p == pal = 1 + barreFila p (pals)
                       | otherwise = barreFila p (pals)



--4)
--cantidadDeApariciones2::(Eq a) => a -> [[a]] -> Integer

--boludez


--5)
multiplicarPorEscalar:: Integer->[[Integer]]->[[Integer]] 
multiplicarPorEscalar lambda [] = []
multiplicarPorEscalar lambda (fila:filas) = barreFilaL lambda (fila):multiplicarPorEscalar lambda (filas)

barreFilaL::Integer->[Integer]->[Integer]
barreFilaL lambda [] = []
barreFilaL lambda (elem:elems) = (lambda*elem):barreFilaL lambda (elems)


--6)

-- concatenarFilas :: [[String]] ->[String]
-- concatenarFilas [] = []
-- concatenarFilas (fila:filas) = creaLista (fila)::creaLista (filas)

-- creaLista::[String]->[String]
-- creaLista [] = []
-- creaLista (pal:pals) = pal:creaLista (pals)


-- concatenarFilas :: [[String]] ->[String]
-- concatenarFilas [] = []
-- concatenarFilas (fila:filas) = creaLista (fila):concatenarFilas (filas)



-- creaLista::[String]->String
-- creaLista [] = []
-- creaLista (col:cols) = col

--agarro una fila y voy metiendo de a una palabra en una lista nueva y asi sucesivamente



--7)
iesimaFila::Integer->[[a]]->[a]
iesimaFila i [] =  []
iesimaFila i m = buscaFila 0 i m


buscaFila::Integer->Integer->[[a]]->[a]
buscaFila _ _ [] = []
buscaFila nFila i (fila:filas) | (nFila == i) = (fila)
                               | otherwise = buscaFila (nFila+1) i (filas)




--8)
iesimaColumna :: Integer -> [[a]] -> [a] 
iesimaColumna i [] = []
iesimaColumna i (fila:filas) = iesimoElemento i 0 (fila)++iesimaColumna i (filas)


iesimoElemento::Integer->Integer->[a]->[a]
iesimoElemento i nElem [] = []
iesimoElemento i nElem (elem:elems) | i == nElem = [elem]
                                    | otherwise = iesimoElemento i (nElem+1) (elems)


--agarro el i-esimo elemento de una fila, paso a la siguiente fila y hago lo mismo


--9)
matrizIdentidad::Integer -> [[Integer]]
matrizIdentidad n = avanzaFila n 0

creaFila::Integer->Integer->Integer->[Integer]
creaFila i dim cont     | cont >= dim  = []
                        | i == cont = 1:creaFila i dim (cont+1)
                        | otherwise = 0:creaFila i dim (cont+1)

avanzaFila::Integer->Integer->[[Integer]]
avanzaFila dim i | i >= dim = []
                 | otherwise = creaFila i dim 0:avanzaFila dim (i+1)



--10)
--cuantos pares hay en la columna i dada una matriz m?
cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna i m = avanzaFila2 i m

avanzaFila2::Integer->[[Integer]]->Integer
avanzaFila2 _ [] = 0 
avanzaFila2 col (fila:filas) | recorreFilaBuscaPar col fila 0 == True = 1 + avanzaFila2 col filas
                            | otherwise = avanzaFila2 col filas


recorreFilaBuscaPar::Integer->[Integer]->Integer->Bool
recorreFilaBuscaPar col (elem:elems) cont | cont /= col = recorreFilaBuscaPar col elems (cont+1)
                                          | otherwise = mod elem 2 == 0