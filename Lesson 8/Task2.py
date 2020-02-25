import requests


def exchange(a, b, c):
    mon1_value = float(a)
    mon1_name = str(b)
    mon2_name = str(c)

    response = requests.get('https://api.exchangerate-api.com/v4/latest/' + mon1_name)
    money_rate = response.json()['rates']
    mon2_value = mon1_value * money_rate.get(mon2_name)

    return mon2_value


print(exchange(10, 'USD', 'RUB'))
