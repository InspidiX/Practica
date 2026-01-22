import os

import json  
with open(r'datos.json') as archivo:    usuarios_data = json.load(archivo) 

for registro in usuarios_data:
    if registro["puntos"] >= 90:
        print(f"{registro['usuario']} tiene un desempeño excelente.")

for  registro in usuarios_data:
    if registro["puntos"] <= 50:
        print(f"{registro['usuario']} debe mejorar su desempeño")

def buscar_usuario(nombre_buscado, lista_datos):
    for registro in lista_datos:
        if registro["usuario"].lower() == nombre_buscado.lower():
            return registro
    return None


def registrar_usuario(lista_datos):
    print("\n--- Registro de nuevo usuario ---")
    nombre = input("Nombre del nuevo usuario: ")

    while True:
    
     try: 
        puntos = int(input("Puntos iniciales: "))
        break
    
     except Exception as e:
        print("Valor incorrecto")
        puntos = 0

    estado = input("Estado: ")
    
    nuevo = {"usuario": nombre, "puntos": puntos, "estado": estado}
    
    lista_datos.append(nuevo)

    with open('datos.json', 'w') as archivo:
        json.dump(lista_datos, archivo, indent=4)

    print(f"¡{nombre} ha sido registrado(a) con éxito!")

def eliminar_usuario(lista_datos):
   print("\n--- ELIMINAR USUARIO ---")
   nombre_a_borrar = input("Escribe el nombre del usuario a borrar: ").lower()

   encontrado = False
   for registro in lista_datos:
       if nombre_a_borrar in registro["usuario"].lower():
          lista_datos.remove(registro)
          encontrado = True
          break
    
   if encontrado:
      with open('datos.json', 'w') as archivo:
          json.dump(lista_datos, archivo, indent=4)
      print(f" Usuario eliminado de la base de datos.")
   else:
      print("No se encontró ninguna coincidencia.")

try:
    with open('datos.json', 'r') as archivo:
        datos = json.load(archivo)

    while True:
      
      total_usuarios = len(datos)
      if total_usuarios == 0:
        print("No hay usuarios registrados")
      elif total_usuarios == 1:
        print(f"{total_usuarios} usuario registrado")
      else:
        print(f"{total_usuarios} usuarios registrados")

      print("\n--- MENÚ DE LA APP ---")
      print("1. Buscar | 2. Registrar | 3. Eliminar | 4. Salir")
      opcion = input("Selecciona: ")
      os.system('cls')

      if opcion == "1":
        nombre = input("¿A quién buscas?: ")
        resultado = buscar_usuario(nombre, datos)
        if resultado:
            print(f"Encontrado: {resultado['usuario']} tiene {resultado['puntos']} puntos.")
        else:
            print("Usuario no registrado.")

      elif opcion == "2":
       
        registrar_usuario(datos) 
      
      elif opcion == "3":

        eliminar_usuario(datos)

      elif opcion == "4":
        print("Saliendo... ¡Guardado completo!")
        break
      
      else:
        print("⚠️ Opción no válida, intenta de nuevo.")

except Exception as e:
    print(f"Error: {e}")