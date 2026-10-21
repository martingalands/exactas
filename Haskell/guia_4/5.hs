--parecido a un while. mientras que n-2*i sea mayor que > 0 hago la productoria

medioFact::Int->Int

medioFact 0 = 1
medioFact n = calculo n (n-n)

calculo n i | cuenta <=2 = cuenta
            | otherwise = cuenta * calculo n (i+1)
            where cuenta = (n-2*i)