import requests
import time

id722=json={
    "Name": "Noivern",
    "Type 1": "Flying",
    "Type 2": "Dragon",
    "Total": 535,
    "HP": 85,
    "Attack": 70,
    "Defense": 80,
    "Sp. Atk": 97,
    "Sp. Def": 80,
    "Speed": 123,
    "Generation": 6,
    "Legendary": "False",
}

id721=json={
    "Name": "Noivern",
    "Type 1": "Flying",
    "Type 2": "Dragon",
    "Total": 535,
    "HP": 85,
    "Attack": 70,
    "Defense": 80,
    "Sp. Atk": 97,
    "Sp. Def": 80,
    "Speed": 123,
    "Generation": 6,
    "Legendary": "False",
}

address = "http://127.0.0.1:5000/"

print("GET Pokemon")
time.sleep(0.5)
get = requests.get('{}pokemon/id700'.format(address))
print(get.text)

print("DELETE Pokemon")
time.sleep(0.5)
delete = requests.delete('{}pokemon/id1'.format(address))
print(delete.text)

print("POST Pokemon")
time.sleep(0.5)
post = requests.post(address+"/pokemon/id1", json=id722)
print(post.text)

print("PUT Pokemon")
time.sleep(0.5)
mod = requests.put('{}pokemon/id721'.format(address), json=id721)