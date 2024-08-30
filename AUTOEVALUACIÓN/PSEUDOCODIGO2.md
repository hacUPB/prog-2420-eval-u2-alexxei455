VARIABLES:
- *altitud_inicial:* Es la altitud desde donde comienza el satélite.
- *coeficiente_arrastre:* Es un valor pequeño que representa la resistencia del aire que afecta al satélite.
- *altitud_minima:* Es la altitud por debajo de la cual se considera que el satélite ha reingresado en la atmósfera y se ha desintegrado.
- *altitud_actual:* Comienza siendo igual a la altitud inicial y se actualiza en cada órbita.
- *orbita_contador:* Cuenta cuántas órbitas completas realiza el satélite.

INICIO


    Mostrar "Ingrese la altitud inicial del satélite (en km):"
    Leer altitud_inicial
    
    Mostrar "Ingrese el coeficiente de arrastre inicial (un valor decimal pequeño, como 0.01):"
    Leer coeficiente_arrastre
    
    Mostrar "Ingrese la altitud mínima de seguridad (en km):"
    Leer altitud_minima
    

    altitud_actual <- altitud_inicial
    orbita_contador <- 0
    

    MIENTRAS (altitud_actual > altitud_minima) HACER
    

        orbita_contador <- orbita_contador + 1
        

        altitud_perdida <- coeficiente_arrastre * altitud_actual
        

        altitud_actual <- altitud_actual - altitud_perdida
        
        coeficiente_arrastre <- coeficiente_arrastre + 0.0001
        
        
        SI (altitud_perdida < 0.001) ENTONCES
            Mostrar "El satélite se ha estabilizado en órbita baja."
            Mostrar "Altitud final: " + altitud_actual + " km"
            Mostrar "Número total de órbitas completadas: " + orbita_contador
            SALIR DEL BUCLE
        FIN SI
    
    FIN MIENTRAS
    

    SI (altitud_actual <= altitud_minima) ENTONCES
        Mostrar "El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado."
        Mostrar "Número total de órbitas completadas: " + orbita_contador
    FIN SI

FIN
