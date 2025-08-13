

print("--Bienvenido--")
print("--MENU.")
print("(1) suma.")
print("(2) resta.")
print("(3) multiplicacion.")
print("(4) division.")

opc = input("Ingrese una opcion: ")

match(opc):
    case "1":
        a = float(input("ingrese un numero: "))
        b = float(input("Igrese su segundo numero: "))
        sum = a + b
        print(f"{a} + {b} = {sum}")
        
match(opc):
    case "2":
        a = float(input("ingrese un numero: "))
        b = float(input("Igrese su segundo numero: "))
        resta = a - b
        print(f"{a} - {b} = {resta}")

match(opc):
    case "3":
        a = float(input("ingrese un numero: "))
        b = float(input("Igrese su segundo numero: "))
        multi = a * b
        print(f"{a} * {b} = {multi}")

match(opc):
    case "4":
        a = float(input("ingrese un numero: "))
        b = float(input("Igrese su segundo numero: "))
        if a == 0 or b == 0:
            print("Te falla no, no se puede divir entre 0")
        else:
            div = a / b
            print(f"{a} / {b} = {div}")