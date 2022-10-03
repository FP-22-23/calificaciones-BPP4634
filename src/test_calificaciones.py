from calificaciones import *

def main():

# Ejercicio 1
    # Apartado a
    notaAda = calcular_nota(30,23,3)

    # Apartado b y c
    totalRespuestas = inputint("¿Cuántas preguntas tiene el test? ")
    aciertos = inputint("¿Cuántas ha acertado? ")
    errores = inputint("¿Cuántas ha fallado? ")
    notaAda = calcular_nota(totalRespuestas,aciertos,errores)
    print("Ada, quien ha acertado", aciertos, "y fallado", errores, "de las", totalRespuestas, "preguntas, ha sacado un", notaAda)


# Ejercicio 2
    # Apartado a
    print(calcula_nota_cuatrimestre((7, 8 ,7), 10, 4.5))

    # Apartado b
    print(calcula_nota_evaluacion_continua((7, 8 ,7, 6, 9, 10), (10, 9), (6, 7)))

    # Apartado c y d
    c1 = inputfloat("¿Cuánto sacó en el primer cuestionario? ")
    c2 = inputfloat("¿Y en el segundo? ")
    c3 = inputfloat("¿Y en el tercero? ")
    c4 = inputfloat("¿Y en el cuarto? ")
    c5 = inputfloat("¿Y en el quinto? ")
    c6 = inputfloat("¿Y en el sexto? ")
    cuestionarios = (c1,c2,c3,c4,c5,c6)
    pa1 = inputfloat("¿Cuánto sacó en el primer parcial? ")
    pa2 = inputfloat("¿Y en el segundo? ")
    parciales = (pa1, pa2)
    pr1 = inputfloat("¿Cuánto sacó en el primer proyecto? ")
    pr2 = inputfloat("¿Y en el segundo? ")
    proyectos = (pr1, pr2)
    notafinal = (calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos))
    print("En ese caso, la nota que ha sacado Ada en la evaluación continua es", notafinal)

if __name__=="__main__":
    main()
