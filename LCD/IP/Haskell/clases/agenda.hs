type Texto = [Char] 
type Nombre = Texto --n
type Telefono = Texto --t
type Contacto = (Nombre, Telefono) --c
--type ContactosTel = [Contacto] --d
type Agenda = [Contacto] --a

--a)enLosContactos::Nombre->ContactosTel->Bool
--b)agregarContacto::Contacto->ContactosTel->ContactosTel

enLosContactos::Nombre->Agenda->Bool

enLosContactos nombre [] = False
enLosContactos nombre ((nombre',telefono):contactos) | nombre == nombre' = True
                                                     | otherwise = enLosContactos nombre contactos


miAgenda = [("Pedro","154315"),("Jose","153513")]


--agregarContacto::Contacto->Agenda->ContactosTel

agregarContacto contacto [] = [(n,t)]
agregarContacto (n,t) ((n',t'):contactos) | n == n' = (n,t):contactos
                                          | otherwise = (n',t'): agregarContacto (n,t) contactos



--nombreEnContacto::Nombre->Contacto->Bool
-- nombreEnContacto n (x:xs) | (n == xs) = True
--                      | otherwise = False

--recorro toda la lista de contactos tel comparando la primera parte del contacto nombre contra nombre

