"""
1- Agregar productos: Permite agregar productos a una lista. Cada producto debe tener un nombre y un precio.
2- Consultar productos: Muestra todos los productos en la lista junto con sus precios.
3-Eliminar productos: Elimina un producto de la lista a partir de su nombre.
4-Menú interactivo: El programa debe ofrecer un menú para que se elija qué acción realizar. Debe incluirse una opción para salir del programa.
"""
list_productos=[]

def menu_inteactivo():
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    while True:
     opcion=input("Ingrese opcion: ")
     if(opcion.isdigit()):
        return(opcion)
     else:
        print("ERROR")
     
    


def agregar_productos(lista):
   while True:
    prod_agregar=str(input("Agrege Producto: ")).capitalize()
    if(prod_agregar=="Salir"):
      break
    else:
   
      precio_prod=float(input("Precio Producto: "))
      list_prod_to=[prod_agregar.capitalize(),precio_prod]
      lista.append(list_prod_to)

def mostrar_productos(lista):
   for i, pd in enumerate(lista):
                print(f"{i+1}- PRODUCTO: {pd[0]}  Precio: {pd[1]} ")
   stop = input("(-----------------ENTER PARA VOLVER AL MENÚ---------------) ")


def Buscar_producto(lista):
   while True:
    producto=input("Que producto deseas buscar?: ")
    if(producto.capitalize()=="Salir"):
       break
    else:
       for i,pd in enumerate(lista):
          if producto==pd[0]:
             print(f"posicion {i+1}, producto: {pd[0]} ,Precio: {pd[1]}")
          else:
             print("NO SE ENCUENTRA")
             continue
           
def borrar_producto(lista):
   while True:
      mostrar_productos(lista)
      producto=input("Que producto desea borrar? ").strip()
      if producto.capitalize()=="Salir":
         break
      for i,pd in enumerate(lista):
         if producto.capitalize()==pd[0]:
            lista.pop(i)
            print("producto eliminado")  
            continue
         
         else:
            print("NO SE ENCONTRO PRODUCTO ")
            continue
   







while True:
   opcion=menu_inteactivo()
   
   match opcion:
      case "1":
         agregar_productos(list_productos)
         continue
      case "2":
         mostrar_productos(list_productos)
         continue
      case "3":
          Buscar_producto(list_productos)
          continue
      case "4":
         borrar_producto(list_productos)
         continue
      case"5":
         print("SALIENDO")
         break
      
         