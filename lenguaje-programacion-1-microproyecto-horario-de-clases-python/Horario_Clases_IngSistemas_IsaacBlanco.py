""" Micro-proyecto Horario de Clases """

# A partir de aquí viene el funcionamiento lógico del horario.
# Horario hehco por el estudiante Isaac Blanco.

print("***************************************************************")
print("'Horarios de la carrera de Ingeniería de Sistemas por semestre'")
print("***************************************************************\n")

print("Listado de codigos pertenecientes a cada semestre")
print("- Semestre 1: 12020")
print("- Semestre 2: 22020")
print("- Semestre 3: 12021")
print("- Semestre 4: 22021")
print("- Semestre 5: 12022")
print("- Semestre 6: 22022")
print("- Semestre 7: 12023")
print("- Semestre 8: 22023")
print("- Semestre 9: 12024")

print(
    "\nPara ver el horario de un estudiante de ese semestre escriba el codigo que se encuentra despúes de los dos puntos\n"
)

Codigo = int(
    input(
        "Escriba el codigo del semestre del cual desee saber las materias, profesores y horario diurno: "
    )
)

if Codigo == 12020:
    print("\nEstudiante: Daniel Tacoa\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "-----",
            "DIBUJT",
            "---------",
            "------",
            "MATTES1",
            "------",
        ],
        [
            "7:45 - 8:30   ",
            "-----",
            "DIBUJT",
            "GEOALNTIC",
            "SEMNR1",
            "MATTES1",
            "SEMNR1",
        ],
        [
            "8:30 - 9:15   ",
            "-----",
            "DIBUJT",
            "GEOALNTIC",
            "SEMNR1",
            "MATTES1",
            "SEMNR1",
        ],
        [
            "9:15 - 10:00  ",
            "-----",
            "------",
            "GEOALNTIC",
            "------",
            "-------",
            "------",
        ],
        [
            "10:00 - 10:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "10:45 - 11:30 ",
            "-----",
            "EDUAMB",
            "---------",
            "HSCTTG",
            "INGLLS1",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "-----",
            "EDUAMB",
            "---------",
            "HSCTTG",
            "INGLLS1",
            "------",
        ],
        [
            "13:00 - 13:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
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

elif Codigo == 22020:
    print("\nEstudiante: James Sanchéz\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "QUIMG",
            "------",
            "---------",
            "------",
            "MATTES1",
            "------",
        ],
        [
            "7:45 - 8:30   ",
            "QUIMG",
            "------",
            "ALJBRALEA",
            "------",
            "MATTES1",
            "------",
        ],
        [
            "8:30 - 9:15   ",
            "QUIMG",
            "------",
            "ALJBRALEA",
            "------",
            "MATTES1",
            "------",
        ],
        [
            "9:15 - 10:00  ",
            "-----",
            "------",
            "ALJBRALEA",
            "SEMNR2",
            "-------",
            "SEMNR2",
        ],
        [
            "10:00 - 10:45 ",
            "-----",
            "FISCS1",
            "---------",
            "SEMNR2",
            "-------",
            "SEMNR2",
        ],
        [
            "10:45 - 11:30 ",
            "-----",
            "FISCS1",
            "---------",
            "INGLS2",
            "-------",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "-----",
            "FISCS1",
            "---------",
            "INGLS2",
            "-------",
            "------",
        ],
        [
            "13:00 - 13:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "MATT2",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "MATT2",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "MATT2",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
    ]

    print(f"Aljebra Lineal: {HorarioC[3][3]} - Profesor Jhon Ledezma")
    print(f"Física I: {HorarioC[5][2]} - Profesor Jhon Ledezma")
    print(f"Ingles II: {HorarioC[7][4]} - Profesora Karen Orochoa")
    print(f"Matemática II: {HorarioC[12][1]} - Profesora Nicolas Adames")
    print(f"Química General: {HorarioC[2][1]} - Profesora Yernay Perez")
    print(f"Seminario II: {HorarioC[5][4]} - Profesor Oliver Mundaray\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 12021:
    print("\nEstudiante: Miriam Bracho\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "-----",
            "PROEST",
            "---------",
            "SSADMT",
            "-------",
            "------",
        ],
        [
            "7:45 - 8:30   ",
            "-----",
            "PROEST",
            "PROGCMACC",
            "SSADMT",
            "-------",
            "------",
        ],
        [
            "8:30 - 9:15   ",
            "-----",
            "PROEST",
            "PROGCMACC",
            "SSADMT",
            "-------",
            "------",
        ],
        [
            "9:15 - 10:00  ",
            "-----",
            "------",
            "PROGCMACC",
            "------",
            "-------",
            "------",
        ],
        [
            "10:00 - 10:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "10:45 - 11:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "13:00 - 13:45 ",
            "FISC2",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "FISC2",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "FISC2",
            "MATTE3",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "-----",
            "MATTE3",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "-----",
            "MATTE3",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
    ]

    print(f"Física II: {HorarioC[9][1]} - Profesor Jhon Ledezma")
    print(f"Matemática III: {HorarioC[11][2]} - Profesor Nicolas Adames")
    print(f"Probabilidad y Estadistica: {HorarioC[1][2]} - Profesora Yernay Perez")
    print(f"Programación: {HorarioC[2][3]} - Profesora Karen Orochoa")
    print(f"Sistemas Administrativos: {HorarioC[1][4]} - Profesor Armando Vegas\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 22021:
    print("\nEstudiante: Marco Quintana\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "-----",
            "LENPR1",
            "---------",
            "------",
            "-------",
            "SSPRDC",
        ],
        [
            "7:45 - 8:30   ",
            "-----",
            "LENPR1",
            "PROCCDATS",
            "------",
            "-------",
            "SSPRDC",
        ],
        [
            "8:30 - 9:15   ",
            "-----",
            "LENPR1",
            "PROCCDATS",
            "------",
            "-------",
            "SSPRDC",
        ],
        [
            "9:15 - 10:00  ",
            "-----",
            "------",
            "PROCCDATS",
            "------",
            "-------",
            "------",
        ],
        [
            "10:00 - 10:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "10:45 - 11:30 ",
            "-----",
            "LOMATT",
            "---------",
            "LOMATT",
            "TEOSSMA",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "-----",
            "LOMATT",
            "---------",
            "LOMATT",
            "TEOSSMA",
            "------",
        ],
        [
            "13:00 - 13:45 ",
            "-----",
            "LOMATT",
            "---------",
            "LOMATT",
            "TEOSSMA",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "CANUM",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "CANUM",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "CANUM",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
    ]

    print(f"Cálculo Numérico: {HorarioC[11][1]} - Profesor Carlos Bastida")
    print(f"Lenguaje de Programación I: {HorarioC[1][2]} - Profesora Lucía Santeramo")
    print(f"Lógica Matemática: {HorarioC[6][2]} - Profesora Enma Valecillos")
    print(f"Procesamiento de Datos: {HorarioC[2][3]} - Profesora Ninoska Cardona")
    print(f"Sistemas de Producción: {HorarioC[1][6]} - Profesor Armando Vegas")
    print(f"Teoría de Sistemas: {HorarioC[6][5]} - Profesor Wilmer Calmauta\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 12022:
    print("\nEstudiante: David Hernandez\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "-----",
            "CILOGG",
            "---------",
            "------",
            "CILOGG ",
            "------",
        ],
        [
            "7:45 - 8:30   ",
            "-----",
            "CILOGG",
            "---------",
            "------",
            "CILOGG ",
            "LENPR2",
        ],
        [
            "8:30 - 9:15   ",
            "-----",
            "CILOGG",
            "---------",
            "------",
            "CILOGG ",
            "LENPR2",
        ],
        [
            "9:15 - 10:00  ",
            "ANDSS",
            "CILOGG",
            "---------",
            "TGGRAF",
            "-------",
            "------",
        ],
        [
            "10:00 - 10:45 ",
            "ANDSS",
            "------",
            "---------",
            "TGGRAF",
            "-------",
            "------",
        ],
        [
            "10:45 - 11:30 ",
            "ANDSS",
            "------",
            "---------",
            "TGGRAF",
            "-------",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "ANDSS",
            "------",
            "---------",
            "TGGRAF",
            "BASDA  ",
            "------",
        ],
        [
            "13:00 - 13:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "BASDA  ",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "BASDA",
            "------",
            "INVESOPER",
            "LENPR2",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "BASDA",
            "------",
            "INVESOPER",
            "LENPR2",
            "-------",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "BASDA",
            "------",
            "INVESOPER",
            "LENPR2",
            "-------",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "BASDA",
            "------",
            "INVESOPER",
            "LENPR2",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
    ]

    print(f"Análisis de Sistemas: {HorarioC[4][1]} - Profesor Wilmer Calmauta")
    print(f"Base de Datos: {HorarioC[10][1]} - Profesora Ninoska Cardona")
    print(f"Circuitos Lógicos: {HorarioC[1][2]} - Profesora Enma Valecillos")
    print(f"Investigación de Operaciones: {HorarioC[9][3]} - Profesor Carlos Bastida")
    print(f"Lenguaje de Programación II: {HorarioC[9][4]} - Profesora Lucía Santeramo")
    print(f"Teoría de Grafos: {HorarioC[4][4]} - Profesora Izamar Barrios\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 22022:
    print("\nEstudiante: Verónica Granados\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "-----",
            "------",
            "OPTLIN   ",
            "------",
            "-------",
            "ARCOM ",
        ],
        [
            "7:45 - 8:30   ",
            "-----",
            "------",
            "OPTLIN   ",
            "------",
            "-------",
            "ARCOM ",
        ],
        [
            "8:30 - 9:15   ",
            "-----",
            "------",
            "OPTLIN   ",
            "------",
            "DÑDSST ",
            "ARCOM ",
        ],
        [
            "9:15 - 10:00  ",
            "-----",
            "------",
            "OPTLIN   ",
            "------",
            "DÑDSST ",
            "------",
        ],
        [
            "10:00 - 10:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "DÑDSST ",
            "------",
        ],
        [
            "10:45 - 11:30 ",
            "ARCOM",
            "------",
            "---------",
            "OPTLIN",
            "-------",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "ARCOM",
            "------",
            "---------",
            "OPTLIN",
            "-------",
            "SSOPTI",
        ],
        [
            "13:00 - 13:45 ",
            "ARCOM",
            "------",
            "---------",
            "OPTLIN",
            "-------",
            "SSOPTI",
        ],
        [
            "13:45 - 14:30 ",
            "ARCOM",
            "------",
            "---------",
            "OPTLIN",
            "-------",
            "SSOPTI",
        ],
        [
            "14:30 - 15:15 ",
            "-----",
            "------",
            "LENPROOG3",
            "------",
            "PROESTS",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "-----",
            "DÑDSST",
            "LENPROOG3",
            "------",
            "PROESTS",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "-----",
            "DÑDSST",
            "LENPROOG3",
            "------",
            "PROESTS",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "DÑDSST",
            "LENPROOG3",
            "------",
            "PROESTS",
            "------",
        ],
    ]

    print(f"Arquitectura del Computador: {HorarioC[6][1]} - Profesora Enma Valecillos")
    print(f"Diseño de Sistemas: {HorarioC[11][2]} - Profesor Wilmer Calmauta")
    print(
        f"Lenguaje de Programación III: {HorarioC[10][3]} - Profesora Lucía Santeramo"
    )
    print(f"Optimización No Lineal: {HorarioC[1][3]} - Profesor Carlos Bastida")
    print(f"Procesos Estocasticos: {HorarioC[10][5]} - Profesor Miguel Jimenez")
    print(f"Sistemas Operativos: {HorarioC[7][6]} - Profesor Miguel Jimenez\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 12023:
    print("\nEstudiante: José Barrientos\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "GRDIN",
            "METDIN",
            "---------",
            "------",
            "METDIN ",
            "------",
        ],
        [
            "7:45 - 8:30   ",
            "GRDIN",
            "METDIN",
            "---------",
            "ELTEC1",
            "METDIN ",
            "------",
        ],
        [
            "8:30 - 9:15   ",
            "GRDIN",
            "METDIN",
            "---------",
            "ELTEC1",
            "METDIN ",
            "------",
        ],
        [
            "9:15 - 10:00  ",
            "INTSS",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "10:00 - 10:45 ",
            "INTSS",
            "RETDDS",
            "---------",
            "------",
            "-------",
            "GRDIN ",
        ],
        [
            "10:45 - 11:30 ",
            "INTSS",
            "RETDDS",
            "---------",
            "ELNTE2",
            "-------",
            "GRDIN ",
        ],
        [
            "11:30 - 12:15 ",
            "-----",
            "RETDDS",
            "---------",
            "ELNTE2",
            "-------",
            "GRDIN ",
        ],
        [
            "13:00 - 13:45 ",
            "-----",
            "------",
            "SINMMULCI",
            "------",
            "-------",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "-----",
            "------",
            "SINMMULCI",
            "------",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "-----",
            "------",
            "SINMMULCI",
            "------",
            "-------",
            "------",
        ],
        [
            "15:15 - 16:00 ",
            "-----",
            "------",
            "SINMMULCI",
            "------",
            "-------",
            "------",
        ],
        [
            "16:00 - 16:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
    ]

    print(f"Gerencia de la Informática: {HorarioC[1][1]} - Profesora Izamar Barrios")
    print(f"Implantación de Sistemas: {HorarioC[4][1]} - Profesora Ninoska Cardona")
    print(f"Metodología de la Investigación: {HorarioC[1][2]} - Profesor Armando Vegas")
    print(f"Redes: {HorarioC[5][2]} - Profesor Miguel Jimenez")
    print(f"Simulación y Modelos: {HorarioC[8][3]} - Profesor Angel Guzman")
    print(f"Electiva Técnica I: {HorarioC[2][4]} - Profesor Melvin Contrera")
    print(f"Electiva No Técnica I: {HorarioC[6][4]} - Profesor Melvin Contrera\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 22023:
    print("\nEstudiante: Isaac Blanco\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "-----",
            "------",
            "TLECPROSC",
            "------",
            "TEODDC ",
            "------",
        ],
        [
            "7:45 - 8:30   ",
            "-----",
            "------",
            "TLECPROSC",
            "------",
            "TEODDC ",
            "MALEI ",
        ],
        [
            "8:30 - 9:15   ",
            "-----",
            "------",
            "TLECPROSC",
            "------",
            "TEODDC ",
            "MALEI ",
        ],
        [
            "9:15 - 10:00  ",
            "AUDSS",
            "------",
            "TLECPROSC",
            "------",
            "TEODDC ",
            "MALEI ",
        ],
        [
            "10:00 - 10:45 ",
            "AUDSS",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "10:45 - 11:30 ",
            "AUDSS",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "11:30 - 12:15 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "13:00 - 13:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "13:45 - 14:30 ",
            "MALEI",
            "AUDSS ",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "14:30 - 15:15 ",
            "MALEI",
            "AUDSS ",
            "---------",
            "TEODDC",
            "ELNTEC2",
            "ELTEC2",
        ],
        [
            "15:15 - 16:00 ",
            "MALEI",
            "AUDSS ",
            "---------",
            "TEODDC",
            "ELNTEC2",
            "ELTEC2",
        ],
        [
            "16:00 - 16:45 ",
            "-----",
            "------",
            "---------",
            "TEODDC",
            "ELNTEC2",
            "ELTEC2",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "TEODDC",
            "-------",
            "------",
        ],
    ]

    print(f"Auditoría de Sistemas: {HorarioC[4][1]} - Profesor Oliver Mundaray")
    print(
        f"Marco Legal para el Ejercicio de la Ingeniería: {HorarioC[9][1]} - Profesor Melvin Contrera"
    )
    print(f"Teleprocesos: {HorarioC[1][3]} - Profesor Angel Guzman")
    print(f"Teoría de las Decisiones: {HorarioC[10][4]} - Profesor Angel Guzman")
    print(f"Electiva Técnica II: {HorarioC[10][6]} - Profesora Izamar Barrios")
    print(f"Electiva No Técnica II: {HorarioC[10][5]} - Profesor Kelvin Centeno\n")

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

elif Codigo == 12024:
    print("\nPasante: Master One\n")
    HorarioC = [
        [
            "Entrada/Salida",
            "LUNES",
            "MARTES",
            "MIERCOLES",
            "JUEVES",
            "VIERNES",
            "SABADO",
        ],
        [
            "7:00 - 7:45   ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "7:45 - 8:30   ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "8:30 - 9:15   ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "9:15 - 10:00  ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "10:00 - 10:45 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "10:45 - 11:30 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "11:30 - 12:15 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "13:00 - 13:45 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "13:45 - 14:30 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "14:30 - 15:15 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "15:15 - 16:00 ",
            "PASST",
            "PASST ",
            "PASST    ",
            "PASST ",
            "PASST  ",
            "PASST ",
        ],
        [
            "16:00 - 16:45 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
        [
            "16:45 - 17:30 ",
            "-----",
            "------",
            "---------",
            "------",
            "-------",
            "------",
        ],
    ]

    print(
        f"Pasantias: {HorarioC[1][4]} - Ingeniero de Sistemas Supervisor Kelvin Centeno\n"
    )

    print(
        f"{HorarioC[0]} \n{HorarioC[1]} \n{HorarioC[2]} \n{HorarioC[3]} \n{HorarioC[4]} \n{HorarioC[5]} \n{HorarioC[6]} \n{HorarioC[7]}"
    )
    print(
        f"{HorarioC[8]} \n{HorarioC[9]} \n{HorarioC[10]} \n{HorarioC[11]} \n{HorarioC[12]} \n{HorarioC[13]}"
    )

else:
    print(
        "\nDebe ingresar uno de los codigos que se encuentran en la lista, de ingresar cualquier otro número el programa no correra."
    )

print(
    "\nSí desea visualizar el horario de un estudiante de alguno de los demás semestres vuelva a ejecutar el programa y consulte en la lista de codigos."
)
