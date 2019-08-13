import os

def graficar(fila,columna,f,c,poss):
    file = open("mapeo.dot","w")
    file.write("digraph H {\n label=\"Mapeo lexicografico\"\r\n node [shape=plaintext]\n " + os.linesep)
    file.write("\tsubgraph cluster_0 {\n\t label=\"Matriz\"\r\n some_node0 [ \n label=<"+os.linesep)
    file.write("\t\t<table border=\"0\" cellborder=\"1\" cellspacing=\"0\">" + os.linesep)
    for i in range(0,fila):
        file.write("\t\t<tr>\n")
        for j in range(0,columna):
            if (i==f)and(j==c):
                file.write("\t\t<td bgcolor=\"#FF5733\">("+str(i)+","+str(j)+")</td>\n")
            else:
                file.write("\t\t<td bgcolor=\"#FFF8DC\">("+str(i)+","+str(j)+")</td>\n")
        file.write("</tr>\n")
    file.write("</table>>" + os.linesep) 
    file.write("];" + os.linesep)   
    file.write("}" + os.linesep)

    file.write("\tsubgraph cluster_1 {\n\t label=\"Arreglo linealizado\"\r\n some_node1 [ \n label=<"+os.linesep)
    file.write("\t\t<table border=\"0\" cellborder=\"1\" cellspacing=\"0\">" + os.linesep)
    file.write("\t\t<tr>\n")
    for i in range(0,(fila*columna)):
        if i==poss:
            file.write("\t\t<td bgcolor=\"#6495ED\">("+str(i)+")</td>\n")
        else:
            file.write("\t\t<td bgcolor=\"#B0E0E6\">("+str(i)+")</td>\n")
    file.write("</tr>\n")
    file.write("</table>>" + os.linesep) 
    file.write("];" + os.linesep)   
    file.write("}" + os.linesep)
    file.write("}" + os.linesep)
    file.close()
    os.system("dot -Tjpg mapeo.dot -o mapeoLX.jpg")
    os.system("mapeoLX.jpg")

def menu():
    for i in range(0,5):
        print("\n")

    print ("Mapeo Lexicografico")
    print ("\t1 - Por filas")
    print ("\t2 - Por columnas")
    print ("\t3 - Salir")

while True:
    menu()
    opcionMenu = input("Opcion: ")
    
    if opcionMenu=="1":
        print ("")
        filas = int(input("Ingrese el numero de filas:"))
        columnas = int(input("Ingrese el numero de columnas:"))
        mat = [None]*(filas*columnas)
        print ("")
        print("Posicion a linealizar:")
        f = int(input("No. fila:"))
        c = int(input("No. columna:"))
        k =int(f*columnas+c)
        print(f"Resultado= {k}")
        graficar(filas,columnas,f,c,k)
        input("\npulsa una tecla para continuar")
        
    elif opcionMenu=="2":
        print ("")
        filas = int(input("Ingrese el numero de filas:"))
        columnas = int(input("Ingrese el numero de columnas:"))
        mat = [None]*(filas*columnas)
        print ("")
        print("Posicion a linealizar:")
        f = int(input("No. fila:"))
        c = int(input("No. columna:"))
        k=int(c*filas+f)
        print(f"Resultado= {k}")
        graficar(filas,columnas,f,c,k)
        input("\npulsa una tecla para continuar")
    elif opcionMenu=="3":
        break
    else:
        print ("")
        input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")