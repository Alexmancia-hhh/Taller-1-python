import os
import time

def celcius_a_fahrenheint(celcius):
    return(celcius * 9/5) + 32
def fahrenheit_a_celcius(fahrenheit):
    return(fahrenheit - 32) * 5/9

flag = True
while flag:
    os.system("cls")
    print("---CONVERTIDOR---")
    print("---menu---")
    print("1) celcius a fahrenheit")
    print("2) fahrenheit a celcius")
    print("3) salir")
    print("----------------------------")

    opc = input("Ingrese una opcion: ")
    os.system("cls")

    match opc:
        case"1":
            grados = float(input("Ingrese en Celcius: "))
            resultado = celcius_a_fahrenheint(grados)
            print(f"{grados} Celcius equivalen a {resultado}")
            os.system("pause")
        case"2":
            grados = float(input("Ingrese en Fahrenheit: "))
            resultado = fahrenheit_a_celcius(grados)
            print(f"{grados} Fahrenheit equivalen a {resultado}") 
            os.system("pause")
        case"0":
            flag = False
            print("Adios bebe")
            time.sleep(3)