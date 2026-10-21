import Prelude

longitud::[t]->Int

longitud [] = 0
longitud (t:ts) = longitud ts +1


ultimo::[t]->[t]

ultimo [] = []
ultimo (t:ts) | longitud ts == 1 = ts
                | otherwise = ultimo ts


principio::[t]->[t]
principio [] = [] 
principio [t] = [t]
principio (t:ts) = principio [t]


anteultimo::[t]->[t]
anteultimo (t:ts) | longitud ts == 1 = ts
                | otherwise = anteultimo (reverse ts)


reverso::[t]->[t]
reverso (t:ts) | longitud ts == 0 = [t]
                | otherwise = (reverso ts) ++ [t]


