type Identificacion = Integer
type Ubicacion = String
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool


-- [
-- (100,(False,"ZD39I")),
-- (101,(True,"JAH3I")),
-- (103,(True,"IQSA9")),
-- (105,(True,"QOTSA")),
-- (109,(False,"893JJ")),
-- (110,(False,"99292"))
-- ]


existeElLocker :: Identificacion ->MapaDeLockers ->Bool
existeElLocker _ [] = False
existeElLocker id ((iL,eL):lockers) | id == iL = True
                                    | otherwise = False || existeElLocker id lockers 


ubicacionDelLocker :: Identificacion ->MapaDeLockers ->Ubicacion
ubicacionDelLocker id ((iL,(dL,uL)):lockers) | id == iL = uL
                                             | otherwise = ubicacionDelLocker id lockers


estaDisponibleElLocker :: Identificacion ->MapaDeLockers ->Bool
estaDisponibleElLocker id ((iL,(dL,uL)):lockers) | id == iL = dL
                                               | otherwise = estaDisponibleElLocker id lockers




--en Haskell las listas son inmutables, por lo que se opta por generar una nueva salida.
ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker id ((iL,(dL,uL)):lockers) | (id == iL) && (dL == True) = (iL,(False,uL)) : lockers  ---aca lo que sucede es que encontre la lista, entonces paso la disponibilidad a False y dejo lo demas como esta (en la lista original)
                                       | otherwise = ((iL),(dL,uL)):ocuparLocker id lockers  --aca lo que hago es dejar el elemento actual como está.

--notar que si no vengo encontrando la lista tengo ((iL),(dL,uL)):ocuparLocker id lockers
--supongo que el siguiente locker sí es el que necesito: viendolo desde el locker anterior queda : ((iL),(dL,uL)):((iL),(False,uL)):lockers
