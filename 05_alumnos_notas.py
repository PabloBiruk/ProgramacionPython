def alumno_notas(alumno, *asignaturas):
    print(f"El alumno {alumno} se ha matriculado de las asignaturas: ")
    print("-----------------------------------------------")
    for a in asignaturas:
        print(a)

asig = ["Programacióin","BD","Sistemas","Filología"]
alumno_notas("miguelito de la Roda", *asig)

# --------------------------------------------

def alumno_notas_2(alumno, *asignaturas, **notas):
    print(f"El alumno {alumno} se ha matriculado de las asignaturas: ")
    print("-----------------------------------------------")
    for a in asignaturas:
        print(a)
    print("-----------------------------------------------")
    print("Sus notas son:")

    for k,v in notas.items():
        print(f" {k}: {v}")


asig = ["Programacióin","BD","Sistemas","Filología"]
notas = {"Programacion":7, "BD":2.5, "Sistemas":5}

alumno_notas_2("Miguelito de la Roda",*asig,**notas )
