import os

def buscadorTXT():
    count = 0
# De la linea [6 - 16] busca archivos con extension .txt, si las encuentra las abre en modo lectura para posteriormente imprimirlas [9 - 14]
    for dirpath, dirnames, filenames in os.walk("."):
        for name in filenames:
            if ".txt" in name:
                print("Archivo", count, ":", os.path.join(dirpath, name))
                fo = open(os.path.join(dirpath, name), "r")
                print("El contenido del archivo es: ")
                i = 1
                for line in fo:               
                    print (i, line)
                    i += 1
                fo.close()            

# De la linea [24 - 28] si se escribe "a" permite añadir informacion al txt
# De la linea [29 - 39] si se escribe "r" permite remover informacion del txt
# De la linea [30 - 32] se abre el txt en modo lectura para leer las lineas y guardarlas en una lista
# De la linea [33 - 35] se abre el txt en modo escritura y se solicita la posicion de la linea a borrar, posteriormente se guarda en la variable linea como posicion de la lista lineas
# La linea [36] elimina la linea segun la variable "linea", de la linea [36 - 38] se reescribe el archivo txt
                op = str(input())
                if op == "a":
                    fo = open(os.path.join(dirpath, name), "a")
                    nURL = input()
                    fo.write("\n" + nURL)
                    fo.close()
                if op == "r":
                    fo = open(os.path.join(dirpath, name), "r")
                    lineas = fo.readlines()
                    fo.close()
                    fo = open(os.path.join(dirpath, name), "w")
                    pos = int(input())
                    linea = lineas[pos]
                    lineas.remove(linea)
                    for linea in lineas:
                        fo.write(linea)
                    fo.close()
                count += 1            
