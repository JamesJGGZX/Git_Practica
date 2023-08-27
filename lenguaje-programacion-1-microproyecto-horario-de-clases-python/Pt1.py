""" Ensayo Lógico """

datos = (1, 2, -1, 1, 0, 1, 2, -1, -1, 2)


def principal(largo, ancho):
    f, c = 0, 0
    for x in range(0, len(datos), 2):
        vx = datos[x]
        vy = datos[x + 1]
        print(vx, vy)
        matriz = [[k] * largo for k in ["O"] * ancho]
        tam = len(matriz)
        print(posicion(vx, vy, tam, f, c))
        f, c = posicion(vx, vy, tam, f, c)
        matriz[f][c] = "X"
        recorrer_matriz(matriz)


def posicion(vx, vy, tam, f=0, c=0):
    f = f + vy
    c = c + vx
    if f >= tam - 1:
        f = tam - 1
    elif f <= 0:
        f = 0
    if c >= tam - 1:
        c = tam - 1
    elif c <= 0:
        c = 0
    return f, c


def recorrer_matriz(mtz):
    for m in mtz:
        print(m)


if __name__ == "__main__":
    print(datos)
    principal(4, 4)
