# Definición de las ciudades, días de la semana y número de semanas
ciudades = ["Quito", "Guayaquil", "Cuenca"]
semanas = 4

# Matriz 3D (Ciudades x Días x Semanas) con temperaturas
arreglo_temperaturas = [
    [  # Quito
        [16, 17, 18, 19, 23, 24, 25],  # semana 1
        [15, 16, 27, 17, 18, 19, 25],  # semana 2
        [10, 12, 14, 16, 26, 28, 29],  # semana 3
        [11, 12, 13, 14, 21, 23, 25],  # semana 4
    ],
    [  # Guayaquil
        [28, 29, 30, 31, 32, 33, 34],  # semana 1
        [25, 26, 27, 28, 29, 30, 31],  # semana 2
        [26, 28, 30, 32, 34, 36, 38],  # semana 3
        [29, 31, 33, 35, 37, 39, 41],  # semana 4
    ],
    [  # Cuenca
        [16, 17, 18, 19, 20, 21, 22],  # semana 1
        [28, 19, 10, 11, 12, 13, 14],  # semana 2
        [10, 12, 14, 16, 18, 20, 22],  # semana 3
        [13, 15, 17, 19, 21, 23, 25],  # semana 4
    ]
]
# Cálculo del promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")
    for semana in range(semanas):
        # Calcular el promedio de temperaturas de la ciudad en la semana
        promedio_semana = sum(arreglo_temperaturas[i][semana]) / len(arreglo_temperaturas[i][semana])
        # Mostrar el resultado
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")

# Definición de la función para calcular la temperatura promedio por ciudad
def promedio_temperatura_por_ciudad(arreglo_temperaturas, ciudades, semanas):
    # Iterar sobre cada ciudad
    for i, ciudad in enumerate(ciudades):
        total_temperatura = 0
        total_dias = 0

        # Calcular la suma de temperaturas de todas las semanas y días para cada ciudad
        for semana in range(semanas):
            total_temperatura += sum(arreglo_temperaturas[i][semana])
            total_dias += len(arreglo_temperaturas[i][semana])

        # Calcular el promedio general para la ciudad
        promedio = total_temperatura / total_dias
        print(f"El promedio de temperatura para {ciudad} durante {semanas} semanas es: {promedio:.2f}°C")

# Llamada a la función
promedio_temperatura_por_ciudad(arreglo_temperaturas, ciudades, semanas)