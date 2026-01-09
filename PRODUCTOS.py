
productos= [("netflix",200,"software"),
            ("canva",500,"software"), 
            ("pera",20,"comestibles")]

USU = None
while USU != 6:
 print("--------------------------------------------------")
 print("|BIENVENIDO                                      |")
 print("--------------------------------------------------")
 print("|1. MOSTRAR TODOS LOS PRODUCTOS CON SUS DATOS    |")
 print("--------------------------------------------------")
 print("|2. BUSCAR UN PRODUCTO POR NOMBRE                |")
 print("--------------------------------------------------")
 print("|3. CONTAR CUANTOS PRODUCTOS HAY DE UNA CATEGORIA|")
 print("--------------------------------------------------")
 print("|4. AGREGAR PRODUCTO                             |")
 print("--------------------------------------------------")
 print("|5. ELIMINAR PRODUCTO                            |")
 print("--------------------------------------------------")
 print("|6. SALIR                                        |")
 print("--------------------------------------------------")
 print("-------------------")
 USU = int(input("|escoja una opcion|"))
 
 
 if USU == 1:
  for i in productos:
     print("--------------------")
     print("|nombre:",i[0]   ,"|")
     print("|precio:",i[1]   ,"|")
     print("|categoria:",i[2],"|")
     print("--------------------")
  
 elif USU == 2:
     pro = False
     print("ESCRIBE EL NOMBRE DEL PRODUCTO A BUSCAR: ")
     product = input("")

     for i in productos:
      if product in i:
       pro = True

     if pro == True:
      print("tu producto está!") 
     else:
        print("tu producto no está!")

     
 elif USU == 3:
   
   categorias_vistas = []
   print("¿DE QUE CATEGORIA ES LA QUE DESEA VER CUANTOS PRODCUTOS HAY")
   for i in productos:
     
     if i[2] not in categorias_vistas:
      categorias_vistas.append(i[2])

   for c in categorias_vistas:
   
    print("categoria: ", c)
   usuario = input("")

   contador = 0
   for i in productos:
    if i[2] == usuario:
      contador+=1
   print("hay",contador,"de productos en la categoria",usuario)
    
   
 elif USU == 4:
   
  nombre = input("escirba el nombre del producto")
  precio = int(input("escriba el precio del producto"))
  categoria = input("escriba la ccategoria del producto")
   
  productos.append((nombre,precio,categoria))
  print("producto agregado!")
  
 
 elif USU == 5:

    for i in productos:
        print("--------------------")
        print("|", i[0], i[1], i[2], "|")
        print("--------------------")

    elim = input("¿Qué producto desea eliminar? ")

    eliminado = False

    for i in productos:
        if i[0] == elim:
            productos.remove(i)
            eliminado = True
            print("Producto eliminado!")
            break

    if not eliminado:
        print("No existe!")

     
