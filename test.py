import requests

service_url = "http://localhost:5004/api/combat/attack"

data = {
    "attacker": {
        "strength" : 12,
        "agility": 8,
        "defense": 5,
    },
    "defender": {
        "health": 100,
        "defense": 3,
        "agility": 6,
        "armor": 2
    },
}

response = requests.post(service_url, json=data)
print(response.json())