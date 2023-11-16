import requests

# Datos JSON que se quieren enviar
json_data = {
    "name": "Ejemplo de artículo",
    "description": "Una descripción de ejemplo",
    "price": 19.99
}

# URL del endpoint
url = "http://127.0.0.1:5000/items/"

# Realizar la solicitud POST con el cuerpo JSON
response = requests.post(url, json=json_data)

# Imprimir la respuesta del servidor
print(response.json())