def naslednjih_7_dni(lat, lon):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude=46.2389&longitude=14.3556&hourly=temperature_2m"
    call = requests.get(base.url).json()

    for i in range(7):
        print(call["daily"]["time"][i])
        