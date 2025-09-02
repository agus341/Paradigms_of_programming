-- Programa simple en Haskell
-- Calcula el factorial de un número ingresado por el usuario

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

main :: IO ()
main = do
    putStrLn "Ingresa un número:"
    input <- getLine
    let n = read input :: Integer
    putStrLn ("El factorial de " ++ show n ++ " es " ++ show (factorial n))
