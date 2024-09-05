#### VARIABLES:
- *titulo:* Título del usuario (Sr. o Sra.).
- *nombre:* Nombre del usuario.
- *apellido:* Apellido del usuario.
- *origen:* Ciudad de origen seleccionada por el usuario.
- *destino:* Ciudad de destino seleccionada por el usuario.
- *dia_semana:* Día de la semana en el que el usuario desea viajar.
- *dia_mes:* Día del mes en el que el usuario desea viajar.
- *distancia:* Distancia entre la ciudad de origen y la ciudad de destino.
- *precio:* Almacena el precio calculado del billete de avión.
- *preferencia_asiento:* Preferencia del usuario para el asiento (pasillo, ventana o sin preferencia).
- *asiento:* Tipo de asiento asignado (A, B, o C).
- *numero_asiento:* Número de asiento aleatorio asignado.

INICIO

    ESCRIBIR "Ingrese su título (Sr. o Sra.): "
    LEER titulo
    ESCRIBIR "Ingrese su nombre: "
    LEER nombre
    ESCRIBIR "Ingrese su apellido: "
    LEER apellido
    ESCRIBIR titulo + nombre + apellido , "¡Bienvenido a FastFast Airlines!"

    ESCRIBIR "Seleccione la ciudad de origen (Medellín, Bogotá, Cartagena): "
    LEER origen
    ESCRIBIR "Seleccione la ciudad de destino (Medellín, Bogotá, Cartagena): "
    LEER destino
    
    SI (origen == "Medellín" Y destino == "Bogotá") O (origen == "Bogotá" Y destino == "Medellín") ENTONCES
        distancia = 240
    SI (origen == "Medellín" Y destino == "Cartagena") O (origen == "Cartagena" Y destino == "Medellín") ENTONCES
        distancia = 461
    SI (origen == "Bogotá" Y destino == "Cartagena") O (origen == "Cartagena" Y destino == "Bogotá") ENTONCES
        distancia = 657
    FIN SI
    
    ESCRIBIR "Ingrese el día de la semana: "
    LEER dia_semana
    ESCRIBIR "Ingrese el día del mes (1-30): "
    LEER dia_mes
    
    SI distancia < 400 ENTONCES
        SI dia_semana == "lunes" O dia_semana == "martes" O dia_semana == "miércoles" O dia_semana == "jueves" ENTONCES
            precio = 79900
        SINO
            precio = 119900
        FIN SI
    SINO
        SI dia_semana == "lunes" O dia_semana == "martes" O dia_semana == "miércoles" O dia_semana == "jueves" ENTONCES
            precio = 156900
        SINO
            precio = 213000
        FIN SI
    FIN SI
    
    ESCRIBIR "El vuelo de " + origen + " a " + destino + " en el día " + dia_semana + ", " + dia_mes + " tendrá un costo de $" + precio
    
    ESCRIBIR "Prefiere asiento en pasillo, ventana o sin preferencia: "
    LEER preferencia_asiento
    
    SI preferencia_asiento == "pasillo" ENTONCES
        asiento = "C"
    SI preferencia_asiento == "ventana" ENTONCES
        asiento = "A"
    SINO
        asiento = "B"
    FIN SI
    
    numero_asiento = GENERAR_NUMERO_ALEATORIO(1, 29)
    ESCRIBIR "Se le ha asignado el asiento " + numero_asiento + asiento + "."
    
FIN
