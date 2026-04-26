import requests
from requests.auth import HTTPDigestAuth

def basic_auth(username, password):
    # Метод Basic Auth
    url = f"https://httpbin.org{username}/{password}"
    response = requests.get(url, auth=(username, password))
    return response.json()

def bear(token):
    # Метод Bearer Token
    url = "https://httpbin.org/bearer"
    jwt_token = f"Bearer {token}"
    headers = {"Authorization": jwt_token}
    response = requests.get(url, headers=headers)
    return response.json()

def digest_auth(username, password):
    # Метод Digest Auth
    url = f"https://httpbin.org{username}/{password}"
    response = requests.get(url, auth=HTTPDigestAuth(username, password))
    return response.json()

# Вставляем ваши данные: veronika и wichg
print(basic_auth(username='veronika', password='wichg'))

# Для Bearer Token я оставил ваш длинный токен из скриншота
print(bear('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'))

print(digest_auth(username='veronika', password='wichg'))
