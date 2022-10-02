from calificaciones import *
'''
totalRespuestas = int(input("¿Cuántas preguntas tiene el test? "))
aciertos = int(input("¿Cuántas ha acertado? "))
errores = int(input("¿Cuántas ha fallado? "))
notaAda = calcular_nota(totalRespuestas,aciertos,errores)
print("Ada, quien ha acertado", aciertos, "y fallado", errores, "de las", totalRespuestas, "preguntas, ha sacado un", notaAda)
'''
print(calcula_nota_cuatrimestre((7, 8 ,7), 10, 6))
print(calcula_nota_evaluacion_continua((7, 8 ,7, 6, 9, 10), (10, 9), (6, 7)))