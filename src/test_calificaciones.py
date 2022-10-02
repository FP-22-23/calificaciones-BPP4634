from calificaciones import *

totalRespuestas = int(input("¿Cuántas preguntas tiene el test? "))
aciertos = int(input("¿Cuántas ha acertado? "))
errores = int(input("¿Cuántas ha fallado? "))
notaAda = calcular_nota(totalRespuestas,aciertos,errores)
print("Ada, quien ha acertado", aciertos, "y fallado", errores, "de las", totalRespuestas, "preguntas, ha sacado un", notaAda)