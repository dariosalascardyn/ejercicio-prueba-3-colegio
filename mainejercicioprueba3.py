from ejercicoprueba3 import registro_estudiante, menu_principal, buscar_estudiante, certificados_estudiante
banderamenu = True
while banderamenu:
    menu_principal()
    opcion = int(input("ingrese opcion\n"))
    try:
        if opcion== 1:
            registro_estudiante()
        elif opcion == 2:
            buscar_estudiante()
        elif opcion == 3:
            certificados_estudiante()
        elif opcion == 4:
            print("saliendo del programa......")
            banderamenu= False
    except:
        print("opcion no valida")
            