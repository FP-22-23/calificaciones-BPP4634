def inputint(mensaje):
    while True:
        res = input(mensaje)
        try:
            return int(res)
        except ValueError:
            print("Por favor, introduzca un número válido.")
        
def inputfloat(mensaje):
    while True:
        res = input(mensaje)
        try:
            res = float(res)
            if 0 <= res <= 10:
                return float(res)
            else:
                print("Por favor, introduzca un número válido.")
        except ValueError:
            print("Por favor, introduzca un número válido.")


# Ejercicio 1
def calcular_nota(totalRespuestas,aciertos,errores):
    nota = aciertos*10/totalRespuestas-errores*10/(50-totalRespuestas)
    return max(nota, 0)


# Ejercicio 2
    # Apartado a
def calcula_nota_cuatrimestre(cuestionarios, parcial, proyecto):
    if proyecto<5:
        return 3
    else:
        return 0.1*sum(cuestionarios)+0.6*parcial+0.1*proyecto

    # Apartado b
def calcula_nota_evaluacion_continua(cuestionarios, parciales, proyecto):
    cuatri1 = calcula_nota_cuatrimestre((cuestionarios[0], cuestionarios[1], cuestionarios[2]), parciales[0], proyecto[0])
    cuatri2 = calcula_nota_cuatrimestre((cuestionarios[3], cuestionarios[4], cuestionarios[5]), parciales[1], proyecto[1])
    if cuatri1<4 or cuatri2<4:
        return 4
    else:
        return (cuatri1+cuatri2)/2