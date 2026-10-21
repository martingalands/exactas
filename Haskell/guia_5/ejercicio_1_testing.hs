--funciona parcialmente, pero no descarta de la lista si ya contó un producto
-- generarStock::[String]->[(String,Int)]
-- generarStock [] = []
-- generarStock (prod:prods) = (prod,cuentaProducto prod (prod:prods)):generarStock (prods)


-- cuentaProducto::String->[String]->Int
-- cuentaProducto prod [] = 0
-- cuentaProducto prod (elem:elems) | (prod == elem) == True = 1 + cuentaProducto prod (elems)
--                                  | otherwise = cuentaProducto prod (elems)




--

generarStock::[String]->[(String,Int)]
generarStock [] = []
generarStock (prod:prods) = (prod,cuentaProducto prod (prod:prods)):generarStock (quitar prod (prods))


cuentaProducto::String->[String]->Int
cuentaProducto prod [] = 0
cuentaProducto prod (elem:elems) | (prod == elem) == True = 1 + cuentaProducto prod (elems)
                                 | otherwise = cuentaProducto prod (elems)



quitar::String->[String]->[String]
quitar art [] = []
quitar art (prod:prods) | (art == prod) == True = quitar art (prods)
                        | otherwise = prod:quitar art (prods)