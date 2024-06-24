import os, time, random
os.system("cls")

estudiantes = []
id_alumnos = []

#funcion menu principal
def menu_principal():
    os.system("cls")
    print("1.- registrar nombre")
    print("2.- buscar estudiante")
    print("3.- imprimir certificados")
    print("4.- salir")
    
#opcion 1 registrar estudiante
def registro_nombre():
    os.system("cls")
    nombre = input("ingrese nombre:\n")
    while len(nombre) < 5:
        nombre = input("ingrese nombre: (debe contener 5 letras al menos)\n")
    return nombre
        
def registro_edad():
    os.system("cls")
    while True:
        edad1 = int(input("ingrese edad:\n"))
        while not edad1:
            edad1 = int(input("ingrese edad:\n"))
        try:
            edad = int(edad1)
            if edad <= 5 or edad >= 18:
                print("edad debe estar entre 12 y 18")
            else:
                return edad         
        except:
            print("en el campo edad no debe venir vacio")
            
def registro_id(contador):
    os.system("cls")
    curso_estudiante = input("ingrese nivel: (basica o media)\n"). lower()
    while curso_estudiante != "basica" and curso_estudiante != "media":
        curso_estudiante = input("ingrese nivel: (basica o media)\n"). lower()
    if curso_estudiante == "basica":
        curso_estudiante = "AB"
        
    elif curso_estudiante == "media":
        curso_estudiante = "AM"
        
    id_final = str(contador).zfill(2) + "-" + curso_estudiante
    contador +=1 
    return id_final

def registro_estudiante():
    os.system("cls")
    print("\t\tREGISTRAR ESTUDIANTE")
    contador = 1
    print("\t\tRegistro estudiante")
    while True:
        nombre =  registro_nombre()
        edad = registro_edad()
        id = registro_id(contador)
        contador += 1
        alumno = [nombre, edad, id]
        estudiantes.append(alumno)
        print(estudiantes)
        try:
            otro_estudiante = int(input("deseas agregar otro alumno?\n 1.-si\n 2.-no\n"))
            while not otro_estudiante:
                otro_estudiante = int(input("deseas agregar otro alumno?\n 1.-si\n 2.-no\n"))
                while otro_estudiante not in [1, 2]:
                    otro_estudiante = int(input("deseas agregar otro alumno?\n 1.-si\n 2.-no\n"))
            if otro_estudiante == 1:
                continue
            else:
                break

        except:
            print("opcion no valida")
    input("ingrese tecla para continar")
    return alumno


#opcion 2 buscar estudiante
def buscar_estudiante():
    os.system("cls")
    print("\t\tBUSCAR ESTUDIANTE")
    id_buscar = input("ingrese su ID de estudiante en el formato (ej: 01-AB)\n").upper()
    for alumno in estudiantes:
        if alumno[2] != id_buscar:
            print("Estudiante no registrado")
            
        elif alumno[2] == id_buscar: 
            print(f"Nombre estudiante: {alumno[0]}")
            print(f"Edad estudiante: {alumno[1]}")
            print(f"ID estudiante: {alumno[2]}")
    input("ingrese tecla para continuar")

#opcion 3 imprimir certificados asistncia, notas, conducta
def certificados_estudiante():
    os.system("cls")
    print("\t\tCERTIFICADOS")
    id_buscar_certf = input("ingrese su ID de estudiante en el formato (ej: 01-AB)\n").upper()
    for alumno in estudiantes:
        if alumno[2] == id_buscar_certf:
            print(f"Nombre estudiante: {alumno[0]}")
            print(f"Edad estudiante: {alumno[1]}")
            print(f"ID estudiante: {alumno[2]}")
            asistencia = random.randint(0, 100)
            nota1 = round(random.uniform(1.0, 7.0), 1)
            nota2 = round(random.uniform(1.0, 7.0), 1)
            nota3 = round(random.uniform(1.0, 7.0), 1)
            promedio = round(((nota1 + nota2 + nota3)/ 3), 1)
            print(f"El porcentaje de asistencia de {alumno[0]} es del {asistencia}%")
            print(f"Nota n° 1: {nota1}")
            print(f"Nota n° 2: {nota2}")
            print(f"Nota n° 3: {nota3}")
            print(f"El promedio de {alumno[0]} es de {promedio}")
            conducta_estudiante(asistencia, promedio)
            input("ingrese tecla para continuar")
        else: 
            print("Estudiante no registrado")
            input("ingrese tecla para continuar")
    return asistencia, promedio,

def conducta_estudiante(asistencia, promedio):
    if (asistencia >= 70 and asistencia <= 100) and (promedio >= 5.0 and promedio <= 7.0):
        print("excelente conducta")
        
    elif (asistencia >= 30 and asistencia < 70) and (promedio >= 3.5 and promedio < 5.0):
        print("Conducta Regular")
        
    elif (asistencia >= 0 and asistencia < 30) and (promedio >= 1.0 and promedio < 3.5):
        print("Mala conducta")
        print("Alumno condicional")
    else:
        print("Conducta Regular")



