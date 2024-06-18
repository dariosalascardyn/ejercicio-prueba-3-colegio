from ejercicoprueba3 import *

banderamenu = True
while banderamenu:
    menu_principal()
    opcion = int(input("ingrese opcion\n"))
    try:
        if opcion== 1:
            registro_estudiante()
        elif opcion == 2:
            print("opcion no valida")
        elif opcion == 3:
            print("opcion no valida")
        elif opcion == 4:
            print("saliendo del programa")
            banderamenu= False
    except:
        print("opcion no valida")
            