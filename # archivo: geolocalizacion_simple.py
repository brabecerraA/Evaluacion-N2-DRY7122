import requests

API_KEY = "84f4153d-13e3-44bc-85d4-7f48d5b719ca"

while True:

    origen = input("Ciudad de Origen (q para salir): ")

    if origen.lower() == "q":
        break

    destino = input("Ciudad de Destino (q para salir): ")

    if destino.lower() == "q":
        break

    # Coordenadas de origen
    url = f"https://graphhopper.com/api/1/geocode?q={origen}&limit=1&key={API_KEY}"
    datos_origen = requests.get(url).json()

    lat1 = datos_origen["hits"][0]["point"]["lat"]
    lon1 = datos_origen["hits"][0]["point"]["lng"]

    # Coordenadas de destino
    url = f"https://graphhopper.com/api/1/geocode?q={destino}&limit=1&key={API_KEY}"
    datos_destino = requests.get(url).json()

    lat2 = datos_destino["hits"][0]["point"]["lat"]
    lon2 = datos_destino["hits"][0]["point"]["lng"]

    # Ruta
    url_ruta = (
        f"https://graphhopper.com/api/1/route?"
        f"point={lat1},{lon1}"
        f"&point={lat2},{lon2}"
        f"&vehicle=car"
        f"&locale=es"
        f"&instructions=true"
        f"&key={API_KEY}"
    )

    ruta = requests.get(url_ruta).json()

    distancia = ruta["paths"][0]["distance"] / 1000
    tiempo = ruta["paths"][0]["time"] / 1000

    horas = tiempo // 3600
    minutos = (tiempo % 3600) // 60
    segundos = tiempo % 60

    combustible = distancia / 12

    print("\nRESULTADOS")
    print(f"Distancia: {distancia:.2f} km")
    print(f"Duración: {horas:.0f} horas, {minutos:.0f} minutos y {segundos:.2f} segundos")
    print(f"Combustible requerido: {combustible:.2f} litros")

    print("\nNarrativa del viaje:")
    for paso in ruta["paths"][0]["instructions"]:
        print("-", paso["text"])

print("Programa finalizado.")