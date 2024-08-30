### ANALISIS DEL PROBLEMA: DESINTEGRACIÓN ORBITAL SATELITE
#### Objetivo del algortimo:
###### Simular la desintegración orbital de un satélite que comienza a una altitud inicial específica y orbita la Tierra en una trayectoria circular. A medida que el satélite desciende, la fuerza de arrastre aumenta, lo que provoca una pérdida de altitud más rápida. El objetivo del algoritmo es simular este proceso hasta que el satélite se estabilice en una órbita baja o reingrese en la atmósfera terrestre.
#### Datos de entrada:
- *Altitud inicial:* La altitud inicial desde la cual el satélite comienza su órbita, medida en kilómetros (km).
 - *Coeficiente de arrastre inicial:* Un pequeño valor decimal que representa la resistencia inicial al movimiento orbital del satélite.
- *Altura miníma de seguridad:* La altitud crítica, medida en kilómetros (km), por debajo de la cual el satélite se desintegrará debido a la reentrada en la atmósfera terrestre.
#### Estructura del algoritmo:
- Solicitar los datos de entrada al usuario
- Iniciar un bucle que simule cada órbita: Calcular la pérdida de altitud,actualizar la altitud actual del satélite, incrementar el coeficiente de arrastre, incrementar el contador de órbitas y comprobar las condiciones de finalización del bucle.
- Mostrar los resultados según las condiciones alcanzadas:
Si el satélite se estabiliza, mostrar la altitud final y el número de órbitas, y si el satélite reingresa, mostrar el mensaje de reingreso y el número total de órbitas.

