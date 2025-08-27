def funcion_externa():
    def do_local():
        var = "local variable"
   
    def do_nonlocal():
        nonlocal var
        var = "nonlocal variable"

    def do_global():
        global var
        var = "global variable"

    var = "variable local"
    
    do_nonlocal()
    print(var)

funcion_externa()