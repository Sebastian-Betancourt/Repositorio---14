# Importación de líbrerías
import os 
import platform
from stdiomask import getpass
from prettytable import PrettyTable


# Definición de varibales globales y constantes
calificacionesTupla=()
calificacionesLista = list(calificacionesTupla)
numCalifi=0


# Definición de funciones 

#Función para limpiar la pantalla
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Función para menú de opciones 
def menu():
     while True:
        print("--------------- SISTEMA SAEW 2.0 -------------")
        print("\n\t\t- Módulo profesor -\n")
        print("-------------------Bienvenido ----------------\n")
        print("¿Qué acción desea realizar?: ")
        print('*  1) Ingresar calificaciones')
        print('*  2) Mostrar calificaciones')
        print('*  3) Detalle de las calificaciones')
        print('*  4) Mostrar detalle de las calificaciones por archivo')
        print('*  5) Mostrar calificaciones de mayor a menor')
        print('*  6) Salir del sistema')
        try:   
            tipoAccion = int(input("Ingrese la opción: "))
            if tipoAccion in [1, 2, 3, 4, 5, 6]:
                return tipoAccion
            else: 
                print("Opción Inválida, Necesita ser un número del 1 al 6.")
        except ValueError:
            print("Opción Inválida, Necesita ser un número del 1 al 6.")

# Función para agregar calificaciones 
def agregarCalificaciones(arreglo,n):
     for i in range(n):
        while True:
            try:
                print(f"Ingrese la calificación final del estudiante {i + 1}: ")
                calificacion = float(input("Calificación: "))
                if 0 <= calificacion <= 20:
                    calificacionesLista.append(calificacion)
                    break
                else:
                    print("Calificación inválida. Debe estar en el rango de 0 a 20.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")


# Función para mostrar calificaciones 
def mostrarCalificaciones(arreglo):
    arreglo.sort()
    print("Las calificaciones registradas son:")
    print(arreglo)

# Función para mostrar calificaciones de mayor a menor
def mostrarCalificacionesMayorMenor(arreglo):
    arreglo.sort(reverse=True)
    print("Las calificaciones registradas de mayor a menor son:")
    print(arreglo)


# Función para guardar información 
def guardarArchivo(data):
    archivo = open("BDD/reporte.txt",'w')
    archivo.write(f'* Detalle de las calificaciones\n')
    archivo.write(f'{data}')
    archivo.close()
    print("Información almacenada exitosamente")


# Función para mostrar información 
def mostrarArchivo():
    archivo = open("BDD/reporte.txt")
    lineas = archivo.readlines()
    for l in lineas:
        print(l,end="")
    archivo.close()


# Función para mostrar detalles de calificaciones 
def mostrarDetalle(arreglo,califi):
    contadorApro=0
    contadorRecha=0
    contadorSuspen=0
    sumCalifi=0
    for i in arreglo:
        sumCalifi += i

    for i in calificacionesLista:
        if 1<=i<=8:
            contadorRecha +=1
        if 9<=i<=13:
            contadorSuspen +=1
        if 14<=i<=20:
            contadorApro +=1

    promedio = round((sumCalifi/califi),2)

    # Crear una instancia de PrettyTable
    tabla = PrettyTable()
    # Definir los encabezados de la tabla
    tabla.field_names = ["Total estudiantes","Promedio", "Aprobados", "Suspensos","Reprobados"]
    # Agregar filas de datos a la tabla
    tabla.add_row([califi,promedio, contadorApro,contadorSuspen,contadorRecha])
    print(tabla)
    guardarArchivo(tabla)


# # Función principal main 
def main():
    password = getpass(prompt="Ingresa tu contraseña: ", mask='*')
    if password == "sistemas":
        limpiar_pantalla()
        caso = menu()
        while caso !=6:
            if caso == 1:
                limpiar_pantalla()
                numCalifi= int(input("Ingrese el número de estudiantes del curso: "))
                agregarCalificaciones(calificacionesLista,numCalifi)
                limpiar_pantalla()
                caso = menu()
            elif caso == 2:
                limpiar_pantalla()
                mostrarCalificaciones(calificacionesLista)
                caso = menu()
            elif caso == 3:
                limpiar_pantalla()
                mostrarDetalle(calificacionesLista,numCalifi)
                caso = menu()
            elif caso == 4:
                limpiar_pantalla()
                mostrarArchivo()
                print()
                caso = menu()
            elif caso ==5:
                limpiar_pantalla()
                mostrarCalificacionesMayorMenor(calificacionesLista)
                caso = menu()

        limpiar_pantalla()
        print("Muchas gracias")

    else:
        print("Usuario no encontrado")



# Ejecutar la función main
main()
