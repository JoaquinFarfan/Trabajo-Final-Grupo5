import numpy as np
import cv2

def mostrar(n,cursos):
    print("  CURSOS",end="")
    for i in range(4):
        print("       ",str(i+1),"BIMESTRE",end="    ")
    print()
    for i in range(6):
        print(cursos[i],"| ",end="      ")
        for j in range(4):
            print(n[i][j],"\t",end="                ")
        print()
    return "COMENTARIO DEL TUTOR: ¡PUEDES SEGUIR MEJORANDO CON MÁS ESFUERZO!"
def datos():
    pregunta = "SI"
    
    while(pregunta == "SI" or pregunta == "si"):

        print("=============== DATOS DEL PADRE RESPONSABLE ===============")

        nom = str(input('Ingrese su Nombre Completo: '))
        apell = str(input('Ingrese su Apellido Completo: '))
        dni = str(input('Ingrese su numero de DNI: '))
        while len(str(dni)) != 8:
            print('Error vuelva a ingresar su numero de DNI: ')
            dni = int(input('Ingrese otra vez su DNI:'))

        print("=============== ID DEL ALUMNO ===============")

        print('Bienvenid@ ', nom,'. A continuación ingrese el id de su hijo: ')
        id_hijo = int(input('Ingrese el ID: '))
        while id_hijo< 1001:
            print('Vuelva a ingresar el ID correcto.')
            id_hijo = int(input('Ingrese el ID: '))
        print("=============== INGRESO CORRECTAMENTE ===============")
        break
def menu():
       
        

        print("          MENU")
        print("<1> CALCULAR SEGUNDO MAYOR")
        print("<2> LOGROS DEL ESTUDIANTE")
        print("<3> SALIR")
def main():
    
    pregunta = "SI"
    list=[]
    while(pregunta == "SI" or pregunta == "si"):
                 

        cursos = ["MATEMATICA"," LENGUAJE ","  INGLES  ","  CIENCIA ","  DEPORTE ","   ARTE   "]
        n = np.random.randint(5,21,size=(6,4))

        opcion = int(input("OPCIÓN: "))
        while(opcion!=3):
            if(opcion == 1):
                print("LAS NOTAS DEL ALUMNO SON: ")
                print("=====================================================================================")
                print(mostrar(n,cursos))
                print("=====================================================================================")
            
            if(opcion == 2):
                print("LOS LOGROS DEL ALMUNO SON:")
                print("=====================================================================================")
                print("Competencias evualuadas:")
                print("1:  Se desenvuelve de manera autónoma a través de su motricidad")
                print("2: Asume una vida saludable")
                print("3:Interactua a traves de sus habilidades sociomotrices")
                print("4:Se comunica oralmente en su lengua materna")
                print("5:Lee diversos tipos de textos escritos en su lengua materna")
                print("6:Escribe diversos tipos de textos en su lengua materna")
                print("7:Aprecia de manera critica manisfestaciones")
                print("8:Crea proyectos desde lenguajes artisticos")
                print("9:Se comunica oralmente en ingles como lengua extranjera")
                print("10:Lee diversos tipos de textos escritos en ingles como lengua extranjera")
                print("11:Escribe diversos tipos de textos escristos en ingles como lengua extranjera")
                print("12:Resuelve problemas de cantidad")
                print("13:Resuelve problemas de regularidad, equivalencia y cambio")
                print("14:Resuelve problemas de forma y movimiento")
                print("15:Resuelve problemas de gestion de datos e incertidumbre")
                print("16:Indaga mediante metodo cientificos para construir sus conocimientos")
                print("17:Explica el mundo fisico basandose en conocimientos sobre los seres vivos,materia y energia")
                print("18:Diseña y construye soluciones tecnologicas para resolver problemas de su entorno")
                print("====================================================================================")
                print("====================================================================================")
                print("====================================================================================")
                print("Área Curricular		Competencias		Calificativos	Calif. comp.	Calif. área")
                print("                         1                 A   A   A           A                    ")
                print("EDUCACION FISICA         2                 A   A   A           A               A    ")
                print("                         3                 A   A   A           A                    ")
                print("====================================================================================")
                print("                         4                 B   A   B           B                    ")
                print("ARTE Y CULTURA           5                 B   B   B           B               B    ")
                print("====================================================================================")
                print("                         6                 A   A   A           A                    ")
                print("INGLES                   7                 B   A   B           B                    ")
                print("                         8                 B   B   B           B               B    ")
                print("====================================================================================")
                print("                         9                 A   A   A           A                    ")
                print("                         10                B   A   B           B                    ")
                print("MATEMATICAS              11                B   B   B           B               B    ")
                print("                         12                A   A   A           A                    ")
                print("====================================================================================")
                print("                         13                B   A   B           B                    ")
                print("COMUNICACION             14                B   B   B           B               B    ")
                print("                         15                A   A   A           A                    ")
                print("====================================================================================")
                print("                         16                B   A   B           B                    ")
                print("CIENCIA Y TECNOLOGIA     17                B   B   B           B               B    ")
                print("                         18                A   A   A           A                    ")
                print("====================================================================================")
            opcion=int(input("INGRESE OTRA OPCIÓN: "))
        if ( opcion==3):
            comentario = input("USTED SALIÓ DEL PROGRAMA, ¿QUIERE DEJAR UN COMENTARIO? SI/NO: ")
            if (comentario == "SI" or comentario == "si"):
                coment = input("COMENTARIO: ")
                list.append(coment)
        pregunta = input("DESEA VER LAS NOTAS DE OTRO ALUMNO SI/NO: ")

    print("===========COMENTARIOS DEL PROGRAMA===========")
    if(len(list)==0):
        print("NO HAY COMENTARIOS")
    u = 1
    for i in list:
        print(u,"|",i)
        u=u+1
def show():
    image = cv2.imread('3322.jpg')
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def principal():
    show()
    datos() 
    menu()
    main()

    
principal()
