import MisFunciones
import Test.HUnit

--Casos de Test
runFibo = runTestTT testsFibo

testsFibo = test [
" Caso base 1: fib 0" ~: (fib 0) ~?= 0,
" Caso base 2: fib 1" ~: (fib 1) ~?= 1,
" Caso recursivo: fib 2" ~: (fib 2) ~?= 2
]

