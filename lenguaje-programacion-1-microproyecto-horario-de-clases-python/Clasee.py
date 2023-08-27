"""Prueba de Escritorio de la idea del horario """

# A partir de aquí viene el funcionamiento del horario
# Esta parte lo que hace es imprimir lo que se encuentra dentro de la lista

print("Estudiante: Daniel Tacoa\n")
HorarioC = [
    ["Entrada/Salida", "LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO"],
    ["7:00 - 7:45   ", "-----", "DIBUJT", "---------", "------", "MATTES1", "------"],
    ["7:45 - 8:30   ", "-----", "DIBUJT", "GEOALNTIC", "SEMNR1", "MATTES1", "SEMNR1"],
    ["8:30 - 9:15   ", "-----", "DIBUJT", "GEOALNTIC", "SEMNR1", "MATTES1", "SEMNR1"],
    ["9:15 - 10:00  ", "-----", "------", "GEOALNTIC", "------", "-------", "------"],
    ["10:00 - 10:45 ", "-----", "------", "---------", "------", "-------", "------"],
    ["10:45 - 11:30 ", "-----", "EDUAMB", "---------", "HSCTTG", "INGLLS1", "------"],
    ["11:30 - 12:15 ", "-----", "EDUAMB", "---------", "HSCTTG", "INGLLS1", "------"],
    ["13:00 - 13:45 ", "-----", "------", "---------", "------", "-------", "------"],
    ["13:45 - 14:30 ", "-----", "------", "---------", "------", "-------", "------"],
    ["14:30 - 15:15 ", "-----", "------", "---------", "------", "-------", "------"],
    ["15:15 - 16:00 ", "-----", "------", "---------", "------", "-------", "------"],
    ["16:00 - 16:45 ", "-----", "------", "---------", "------", "-------", "------"],
    ["16:45 - 17:30 ", "-----", "------", "---------", "------", "-------", "------"],
]

print(f"Dibujo: {HorarioC[2][2]} - Profesor Denny Colina")
print(f"Eduación Ambiental: {HorarioC[7][2]} - Profesor Denny Colina")
print(f"Geometría Analítica: {HorarioC[3][3]} - Profesor Denny Colina")
print(
    f"Hombre, Sociedad, Ciencia y Tecnología: {HorarioC[7][4]} - Profesora Yernay Perez"
)
print(f"Ingles I: {HorarioC[7][5]} - Profesora Karen Orochoa")
print(f"Matemática I: {HorarioC[1][5]} - Profesor Nicolas Adames")
print(f"Seminario I: {HorarioC[3][4]} - Profesor Oliver Mundaray\n")

print(
    f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
)
print(
    f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
)
