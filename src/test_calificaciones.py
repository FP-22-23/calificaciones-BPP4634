from calificaciones import *

def main():

# Ejercicio 1
    # Apartado a
    notaAda = print("Ada ha sacado un", calcular_nota(30,23,3))

    # Apartado b y c
    nombreal = input("Introduzca el nombre del alumno/a: ")
    totalRespuestas = inputint("¿Cuántas preguntas tiene el test? ")
    aciertos = inputint("¿Cuántas ha acertado? ")
    errores = inputint("¿Cuántas ha fallado? ")
    notaAda = calcular_nota(totalRespuestas,aciertos,errores)
    print(nombreal + ", quien ha acertado", aciertos, "y fallado", errores, "de las", totalRespuestas, "preguntas, ha sacado un", notaAda)


# Ejercicio 2
    # Apartado a
    print("Test de la función 'calcula_nota_cuatrimestre':", calcula_nota_cuatrimestre((7, 8 ,7), 10, 4.5))

    # Apartado b
    print("Test de la función 'calcula_nota_evaluacion_continua':", calcula_nota_evaluacion_continua((7, 8 ,7, 6, 9, 10), (10, 9), (6, 7)))

    # Apartado c y d
    nombreal = input("Introduzca el nombre del alumno/a: ")
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
    print("En ese caso, la nota que ha sacado " + nombreal + " en la evaluación continua es un", notafinal)

if __name__=="__main__":
    main()
