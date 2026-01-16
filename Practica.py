import json  
with open(r'C:\Users\Politicas P 1\Documents\Ruben\Programacion\datos.json') as archivo:    infoapp_data = json.load(archivo) # Cargamos los datos en la variable

print(f"Se han cargado {len(infoapp_data)} registros desde la base de datos.")

for registro in infoapp_data:
    if registro["puntos"] >= 90:
        print(f"{registro['usuario']} tiene un desempeño excelente.")

def buscar_usuario(nombre_buscado, lista_datos):
    for registro in lista_datos:
        if registro["usuario"].lower() == nombre_buscado.lower():
            return registro
    return None

try:
    with open('datos.json', 'r') as archivo:
        datos = json.load(archivo)

    usuario_a_buscar = input("¿A Quien buscas en la App?: ")
    resultado = buscar_usuario(usuario_a_buscar, datos)

    if resultado:
        print(f"Encontrado: {resultado['usuario']} de {resultado['estado']} tiene {resultado['puntos']} puntos.")
    else:
        print(" Usuario no registrado en la base de datos.")

except Exception as e:
    print(f"Error: {e}")