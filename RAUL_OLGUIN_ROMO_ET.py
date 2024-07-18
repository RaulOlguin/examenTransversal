import random
import csv


trabajadores = ['Juan Perez' , 'Maria Garcia' , 'Carlos Lopez' , 'Ana Martinez' ,
                 'Pedro Rodriguez', 'Laura Hernandez' , 'Miguel Sanchez' , 'Isabel Gomez' ,
                 'Francisco Diaz' , 'Elena Fernandez' ]

# arreglo de diccionarios
# cada diccionario sera un trabajador con sus datos.
datos_trabajadores = []


# funcion asigna sueldos a trabajadores en un arreglo de diccionarios, calcula el porcentaje de salud, afp y sueldo liquido
# ademas prepara el arreglo para ser impreso en un csv 
def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo = random.randrange(300_000, 2_500_000)
        salud = round((sueldo * 0.07),2)
        afp = round((sueldo * 0.12),2)
        datos_trabajadores.append({'nombre':trabajador, 'sueldo':sueldo, 'salud':salud, 'afp':afp, 'sueldo_liquido':round(((sueldo - salud) - afp),2)})


# contar sueldo y mostrar son parte de clasificar sueldos
# inclusivo: cuando es True incluye los sueldos en el rango a contar
        
# contar_sueldo retorna cuantos trabajadores hay con el rango dado
def contar_sueldos(inicio = 0, fin = 800_000, inclusivo = False):
    contador = 0
    for trabajador in datos_trabajadores:
        if inclusivo:
            if inicio <= trabajador['sueldo'] <= fin:
                contador += 1
        else:
            if inicio < trabajador['sueldo'] < fin:
                contador += 1
    return contador

# mostrar genera lista de trabajadores y sus sueldos en el rango dado
def mostrar(inicio = 0, fin = 800_000, inclusivo = False):
    print("Nombre empleado\t\tSueldo")
    for trabajador in datos_trabajadores:
        if inclusivo:
            if inicio <= trabajador['sueldo'] <= fin:
                print(f"{trabajador['nombre']}\t\t{trabajador['sueldo']}")
        else:
            if inicio < trabajador['sueldo'] < fin:
                print(f"{trabajador['nombre']}\t\t{trabajador['sueldo']}")

# calculo de la media geometrica para la funcion estadistica
def media_geometrica(arreglo):
    for sueldo in arreglo:
        sueldo *= sueldo
    return sueldo**(1/len(arreglo))

# entrega la estadisticas solicitada
# genera un arreglo con los sueldos y a partir de ello genera las estadisticas 
def estadisticas():
    sueldos = []
    for datos in datos_trabajadores:
        sueldos.append(datos['sueldo'])
    
    print(f"\tsueldo mas alto : {max(sueldos)}\n\tsueldo mas bajo: {min(sueldos)}\n\tsueldo promedio: {(sum(sueldos)/len(sueldos))}\n\tmedia geometrica: {media_geometrica(sueldos)}")

# genera csv con la nomina de los trabajadores.
# el diccionario cuando se inicializo se dejo en el formato requerido para ser trabajado por dictwriter del modulo csv  
def exportar_csv():

    with open('Listado_Trabajadores.csv', 'w', newline='') as archivo:
        cabecera = ['nombre', 'sueldo', 'salud', 'afp', 'sueldo_liquido']
        escritor = csv.DictWriter(archivo, fieldnames=cabecera, dialect='excel', delimiter=';')

        escritor.writeheader()
        escritor.writerows(datos_trabajadores)

        print("\n\t CSV GENERADO \n\n")


# Menu  
while True:

    print("\n\n\t*** MENU PRINCIPAL ***\n\n")

    print(""" 
        1. Asignar sueldos aleatorios
        2. Clasificar sueldos
        3. Ver estadísticas.
        4. Reporte de sueldos
        5. Salir del programa
    """)

    try:
        opcion = int(input("\tingrese su opcion >> "))
    except(ValueError, SyntaxError):
        opcion = -1
    except:
        opcion = -1


    if opcion == 5:
        print("\n\tFinalizando programa ...\n\tDesarrollado por Raul Olguin\n\tRUT 15.431.248-K\n\n\n")
        break
    elif opcion == 1:
        if datos_trabajadores:
            print("\n\n\tUsted ya ha asignado sueldos\n\n")
            input("\n\n\tPresione ENTER para continuar\n\n")
        else:
            asignar_sueldos()
            print("\n\n\tLos sueldos han sido asignados\n\n")
            input("\n\n\tPresione ENTER para continuar\n\n")
    
    elif opcion == 2:

        if datos_trabajadores:
            print("\n\n\t*** MENU CLASIFICAR SUELDOS ***\n\n")

            print(f"Sueldos menores a $800.000 TOTAL: {contar_sueldos()} \n")
            mostrar()

            print(f"\n\nSueldos entre $800.000 y 2.000.000 TOTAL: {contar_sueldos(800_000,2_000_000, True)} \n")
            mostrar(800_000, 2_000_000, True)

            print(f"\n\nSueldos superiores a 2.000.000 TOTAL: {contar_sueldos(2_000_000, 2_500_000)} \n")
            mostrar(2_000_000, 2_500_000)


            input("\n\n\tPresione ENTER para continuar\n\n")
        else:
            print("\n\n\tPara continuar Asigne sueldos\n\n")
            input("\n\n\tPresione ENTER para continuar\n\n")

    elif opcion == 3:
         
        if datos_trabajadores:
            print("\n\n\t*** MENU ESTADISTICA ***\n\n")
            estadisticas()
            

            input("\n\n\tPresione ENTER para continuar\n\n")
        else:
            print("\n\n\tPara continuar Asigne sueldos\n\n")
            input("\n\n\tPresione ENTER para continuar\n\n")

    elif opcion == 4:

        if datos_trabajadores:
            print("\n\n\t*** MENU REPORTE DE SUELDO ***\n\n")
            exportar_csv()
            

            input("\n\n\tPresione ENTER para continuar\n\n")
        else:
            print("\n\n\tPara continuar Asigne sueldos\n\n")
            input("\n\n\tPresione ENTER para continuar\n\n")

    else:
        print("\n\n\tIngrese opcion Valida\n\n")
    