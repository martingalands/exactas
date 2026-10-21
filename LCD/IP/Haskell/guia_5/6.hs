type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos ::Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((nomCont,telCont):contactos) | nombre == nomCont = True
                                                              | otherwise = False || enLosContactos nombre contactos


agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (nom,tel) [] = [(nom,tel)]
agregarContacto (nom,tel) ((nomCont,telCont):conts) | nom == nomCont = (nomCont,telCont):agregarContacto (nom,tel) conts
                                                    | otherwise = (nomCont,telCont):agregarContacto (nom,tel) conts



eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nom ((nomCont,telCont):conts) | nom == nomCont = eliminarContacto nom conts
                                               | otherwise = (nomCont,telCont):eliminarContacto nom conts

