import requests
def naslednjih_7_dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&hourly=temperature_2m"
    call = requests.get(base.url).json()

    for i in range(7):
        print(call["daily"]["time"][i])

def trenutna_temp2(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
        "timezone": "auto",
        "forecast_days": 1
    }

    call = requests.get(base_url, params=params)
    print(call.url)

    json_data = call.json()
    return json_data["current"]["temperature_2m"]


cities = [
    ("Ljubljana", 46.0511, 14.5051),
    ("Maribor", 46.5558, 15.6459),
    ("Celje", 46.2309, 15.2604),
    ("Kranj", 46.2389, 14.3556),
]

mestav = []

for c in cities:
    temp = trenutna_temp2(c[1], c[2])
    print(temp, c[0])
    mestav.append(temp)

print("Najvišja temperatura:", max(mestav))
