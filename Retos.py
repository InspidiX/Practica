import json

def
with open(r'C:\Users\Politicas P 1\Documents\Ruben\Programacion\datos.json') as archivo: datos = json.load(archivo)

while True:
    usuario_a_buscar = input("\n¿A quien Buscas? (Escribe 'salir' para terminar): ")

    if usuario_a_buscar.lower() == 'salir':
        print("¡Gracias por usar mi App!")
        break 

    resultado = buscar_usuario(usuario_a_buscar, datos)

    if resultado:
        print(f"✅ Usuario: {resultado['usuario']} | Puntos: {resultado['puntos']} | Estado: {resultado['estado']}")
    else:
        print("❌ No se encontró a ese usuario.")