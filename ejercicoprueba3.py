import os, time
os.system("cls")

estudiantes = []
id_alumnos = []
contador = 0

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
            
def registro_id():
    os.system("cls")
    curso_estudiante = input("ingrese nivel: (basica o media)\n"). lower()
    while curso_estudiante != "basica" and curso_estudiante != "media":
        curso_estudiante = input("ingrese nivel: (basica o media)\n"). lower()
    if curso_estudiante == "basica":
        curso_estudiante = "AB"
        
    elif curso_estudiante == "media":
        curso_estudiante = "AM"
        
    id_final = str(contador + 1).zfill(2) + "-" + curso_estudiante
    return id_final

def registro_estudiante():
    os.system("cls")
    print("\t\tRegistro estudiante")
    while True:
        nombre =  registro_nombre()
        edad = registro_edad()
        id = registro_id()
        alumno = [nombre, edad, id]
        estudiantes.append(alumno)
        try:
            if input("deseas agregar otro alumno?\n 1.-si\n 2.-no\n"):
                break
            else:
                continue
        except:
            print("opcion no valida")
    print(estudiantes)
    input("ingrese tecla para continar")
                
#opcion 2 buscar estudiante
def buscar_estudiante():
    
               
                
        
                
        
        
    
    