import requests


def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print("Something wrong =(")


if __name__ == '__main__':
	data = get_weather('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=09f30bfbf070a37e06c0aa3c13e6fbef')
	print(data)
