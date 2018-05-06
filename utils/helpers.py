import asyncio
import aiohttp
import json
import urllib.parse as to_url

from . import config

def owm_icon_set(icon):
    return {
        'Clear': ':sunny:',
        'Clouds': ':cloud:',
        'Thunderstorm': ':thunder_cloud_rain:',
        'Drizzle': ':white_sun_rain_cloud:',
        'Rain': ':cloud_rain:',
        'Snow': ':cloud_snow:',
        'Atmosphere': ':earth_americas:'
    }.get(icon)

def set_yh_data(c):
	code = int(c)
	data = {}

	tornado = [0]
	storm = [1,2,3,4,23,37,38,39,45,47]
	drizzle = [8,9,11,12]
	rain = [5,6,10,35,40]
	snow = [7,13,14,15,16,17,18,41,42,43,46]
	cloudy = [26,27,28,29,30,44]
	clear = [31,32,33,34,36]
	others = [19,20,21,22,23,24,25]

	if code in tornado:
		data["icon"] = ":tornado:"
		data["desc"] = "Tornado"
		return data

	elif code in storm:
		data["icon"] = ":thunder_cloud_rain:"
		if code == 1:
			data["desc"] = "Tormenta tropical"
		elif code == 2:
			data["desc"] = "Huracan"
		elif code == 3:
			data["desc"] = "Tormentas eléctricas severas"
		elif code == 4:
			data["desc"] = "Tormentas eléctricas"
		elif code == 23:
			data["desc"] = "Borrascoso"
		elif code == 37:
			data["desc"] = "Tormentas eléctricas aisladas"
		elif code == 38:
			data["desc"] = "Tormentas eléctricas dispersas"
		elif code == 39:
			data["desc"] = "Tormentas eléctricas dispersas"
		elif code == 45:
			data["desc"] = "Chubascos con relámpagos"
		elif code == 47:
			data["desc"] = "Chubascos aislados con relámpagos"

		return data

	elif code in drizzle:
		data["icon"] = ":white_sun_rain_cloud:"
		if code == 8:
			data["desc"] = "Llovizna helada"
		elif code == 9:
			data["desc"] = "Llovizna"
		elif code == 11:
			data["desc"] = "Chubascos"
		elif code == 12:
			data["desc"] = "Chubascos"

		return data

	elif code in rain:
		data["icon"] = ":cloud_rain:"
		if code == 5:
			data["desc"] = "Lluvia y nevada mezcladas"
		elif code == 6:
			data["desc"] = "Lluvia y aguanieve mezcladas"
		elif code == 10:
			data["desc"] = "Lluvia helada"
		elif code == 35:
			data["desc"] = "Lluvia y granizo mezclados"
		elif code == 40:
			data["desc"] = "Chubascos dispersos"

		return data

	elif code in snow:
		data["icon"] = ":cloud_snow:"
		if code == 7:
			data["desc"] = "Nevadas y aguanieve mezcladas"
		elif code == 13:
			data["desc"] = "Copos de nieve"
		elif code == 14:
			data["desc"] = "Nevadas ligeras"
		elif code == 15:
			data["desc"] = "Ventiscas de nieve"
		elif code == 16:
			data["desc"] = "Nieve"
		elif code == 17:
			data["desc"] = "Granizo"
		elif code == 18:
			data["desc"] = "Aguanieve"
		elif code == 41:
			data["desc"] = "Fuertes nevadas"
		elif code == 42:
			data["desc"] = "Chubascos de nieve dispersos"
		elif code == 43:
			data["desc"] = "Fuertes nevadas"
		elif code == 46:
			data["desc"] = "Chubascos de nieve"
		
		return data

	elif code in cloudy:
		data["icon"] = ":cloud:"
		if code == 26:
			data["desc"] = "Nublado"
		elif code == 27:
			data["desc"] = "Mayormente nublado (día)"
		elif code == 28:
			data["desc"] = "Mayormente nublado (noche)"
		elif code == 29:
			data["desc"] = "Parcialmente nublado (día)"
		elif code == 30:
			data["desc"] = "Parcialmente nublado (noche)"
		elif code == 44:
			data["desc"] = "Parcialmente nublado"
		return data

	elif code in clear:
		data["icon"] = ":sunny:"
		if code == 31:
			data["desc"] = "Despejado"
		elif code == 32:
			data["desc"] = "Soleado"
		elif code == 33:
			data["desc"] = "Despejado (noche)"
		elif code == 34:
			data["desc"] = "Despejado (día)"
		elif code == 36:
			data["desc"] = "Cálido"

		return data

	elif code in others:
		data["icon"] = ":fog:"
		if code == 19:
			data["desc"] = "Polvaderas"
		elif code == 20:
			data["desc"] = "Brumoso"
		elif code == 21:
			data["desc"] = "Neblina"
		elif code == 22:
			data["desc"] = "Humoso"
		elif code == 24:
			data["desc"] = "Ventoso"
		elif code == 25:
			data["desc"] = "Frío"

		return data
	else:
		data["icon"] = ":no_entry_sign:"
		data["desc"] = "No encontrado"
		return data

async def clima_owm(city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={key}&units=metric&lang=es'.format(ciudad=city, key=config["api"]["key"]["OWM"])
	async with aiohttp.ClientSession() as session:  # Async HTTP request
		raw_response = await session.get(url)
		response = await raw_response.json()
		if response["cod"] == 200:
			return ("\n:flag_{flag}: **| Clima actual en {city}, {country} **\n"
						        "**Clima:** {icon} ({desc})\n"
						        "**Temp:** {temp} °C  **Min:** {min} °C  **Max:** {max} °C\n"
						        "**Humedad:** {hum}% **Viento:** {wind} m/s\n").format(flag=response["sys"]["country"].lower(), city=response["name"], country=response["sys"]["country"], icon=owm_icon_set(response["weather"][0]["main"]), desc=response["weather"][0]["description"], temp=response["main"]["temp"], min=response["main"]["temp_min"], max=response["main"]["temp_max"], hum=response["main"]["humidity"], wind=response["wind"]["speed"])
		else:
			return "**No se pudo encontrar información de esa ciudad** *...pta ke sed*"

async def clima_yh(city):
	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='{city}') and u='c'".format(city=city)
	url = baseurl + to_url.urlencode({'q':yql_query}) + "&format=json"
	async with aiohttp.ClientSession() as session:  # Async HTTP request
		raw_response = await session.get(url)
		response = await raw_response.json()
		if response["query"]["results"] is not None:
			res = response["query"]["results"]["channel"]
			title = res["title"].replace('Yahoo! Weather for ', '')
			splitted_title = title.split(",")
			flag = splitted_title[2].replace(' ', '').lower()
			ico = set_yh_data(res["item"]["condition"]["code"])
			return ("\n:flag_{flag}: **| Clima actual en {city}, {state}, {country} **\n"
						        "**Clima:** {icon} ({desc})\n"
						        "**Temp:** {temp} °C  **Min:** {min} °C  **Max:** {max} °C\n"
						        "**Humedad:** {hum}% **Viento:** {wind} km/h\n").format(flag=flag, city=res["location"]["city"], state=res["location"]["region"], country=res["location"]["country"], icon=ico["icon"], desc=ico["desc"], temp=res["item"]["condition"]["temp"], min=res["item"]["forecast"][0]["low"], max=res["item"]["forecast"][0]["high"], hum=res["atmosphere"]["humidity"], wind=res["wind"]["speed"])
		else:
			return "**No se pudo encontrar información de esa ciudad** *...pta ke sed*"