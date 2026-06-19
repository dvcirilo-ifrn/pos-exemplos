import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass()
api_url = "https://api.github.com"

def gh_list():
    code = 200
    lista = []
    page = 1
    while code == 200:
        response = requests.get(f"{api_url}/user/followers?page={page}&per_page=10",
                auth = HTTPBasicAuth(user , password))
        code = response.status_code
        if code == 200:
            print(response.json())
            lista.append(response.json())
            page += 1
    return lista

def gh_follow(username):
    response = requests.put(f"{api_url}/user/following/{username}",
            auth = HTTPBasicAuth(user , password))
    return response.status_code == 204

def gh_unfollow(username):
    response = requests.delete(f"{api_url}/user/following/{username}",
            auth = HTTPBasicAuth(user , password))
    return response.status_code == 204

op = input("Digite 1 para listar seus seguidores, 2 para seguir e 3 para deixar de seguir um usuário: ") 
if op == "1":
    for seguidor in gh_list():
        print(seguidor["login"])
elif op == "2":
    user_to_follow = input("Digite o username para seguir: ")
    if gh_follow(user_to_follow):
        print(f"{user_to_follow} seguido com sucesso!")
    else:
        print("Deu ruim :(")
elif op == "3":
    user_to_unfollow = input("Digite o username para seguir: ")
    if gh_follow(user_to_unfollow):
        print(f"Você deixou de seguir {user_to_unfollow} com sucesso!")
    else:
        print("Deu ruim :(")
else:
    print("Opção inválida")

