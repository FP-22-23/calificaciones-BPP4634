def calcular_nota(totalRespuestas,aciertos,errores):
    nota = aciertos*10/totalRespuestas-errores*10/(50-totalRespuestas)
    if nota < 0:
        nota = 0
    return nota