"""

Juan Felipe Hernández Quintero - 2241796
Johan Francisco López Jaimes - 2241548

"""

from bigtree import Node, print_tree

#Nodo raíz
raiz = Node("Computador")

#Nivel 1
hardware = Node("Hardware", parent = raiz)
software = Node("Software", parent = raiz)

#Nivel 2
procesador = Node("Procesador (CPU)", parent = hardware)
memoria = Node("Memoria RAM", parent = hardware)
almacenamiento = Node("Almacenamiento", parent = hardware)
perifericos = Node("Periféricos", parent = hardware)

#Nivel 3
Node("Intel Core i5", parent = procesador)
Node("AMD Ryzen 7", parent = procesador)

Node("8GB DDR4", parent = memoria)
Node("16GB DDR3", parent = memoria)

Node("SSD 512GB", parent = almacenamiento)
Node("HDD 1TB", parent = almacenamiento)

Node("Teclado", parent = perifericos)
Node("Mouse", parent = perifericos)
Node("Monitor", parent = perifericos)

#Nivel 2
sistemaOperativo = Node("Sistema Operativo", parent = software)
aplicaciones = Node("Aplicaciones", parent = software)
drivers = Node("Drivers", parent = software)

#Nivel 3
Node("Windows 10", parent = sistemaOperativo)
Node("ArchLinux", parent = sistemaOperativo)

Node("Microsoft Office", parent = aplicaciones)
Node("Google Chrome", parent = aplicaciones)
Node("VS Code", parent = aplicaciones)

Node("Driver de impresora", parent = drivers)
Node("Driver de video", parent = drivers)


#---------- Imprimir ----------
print_tree(raiz)
