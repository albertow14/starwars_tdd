### Condiciones
    .- Lo primero que hacemos es llamar a la api con el endpoint /people. Nos da un json con una key que es count, ahora hacemos una llamada al endpoint de planets que son 61.
    
    Con este numero luego tendremos que generar un numero aleatorio
     ( con esto generamos un numero random,)
    .- Se hace una llamada al numero random mas la api. Nos devuelve una persona nos intersa, name, mass, homeworld
    .- Ahora vamos a visitar un planeta random no puede tocarle el mismo planeta. de este planeta nos interesa el nombre y la gravedad (gravity) nos quedaremos con el primer numero. Este numero lo multiplicaremos por 10 y a su vez por la masa del personaje, con ese dato cogemos el dato de su planeta natal cogiendo masa y nombre. Con esto hacemos una comparación. El resultado final es un JSON contendra la frase "{nombre_persona,} pesa {X} en su planeta natal y pesa {X} en el {planeta_random}.


    Posibles problemas.
    Dato que sea unknow ---> si se desconoce la masa del personaje que pare (se retorna no tiene masa conocida).


    
