import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error al obtener el JSON: {response.status_code}')

def send_telegram_message(message, token, chat_id):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(url, data=payload)

def main():
    months_data = [
        {'months': ['07', '09', '11'], 'year': '2025'},
        {'months': ['01', '03', '05'], 'year': '2026'}
    ]
    all_day_prices = []
    min_price = 600 # Precio mínimo para enviar notificación
    telegram_token = os.getenv('telegram_token')
    telegram_chat_id = os.getenv('telegram_chat_id')

    for year_data in months_data:
        for month in year_data['months']:
            response = get_request(
                f'https://www.flylevel.com/nwe/flights/api/calendar/?triptype=RT&origin=EZE&destination=BCN&month={month}&year={year_data["year"]}&currencyCode=USD'
            )
            if response and 'data' in response and 'dayPrices' in response['data']:
                valid_prices = [p for p in response['data']['dayPrices'] if p['price'] is not None]
                all_day_prices.extend(valid_prices)
            else:
                print(f"Datos no encontrados para el mes {month} del año {year_data['year']}")

    if all_day_prices:
        top_10 = sorted(all_day_prices, key=lambda x: x['price'])[:1]

        print(json.dumps({'dayPrices': top_10}, indent=2))

        for price_info in top_10:
            if price_info['price'] < min_price:
                message = (
                    f"¡Precio bajo encontrado! {price_info['price']} USD para la fecha {price_info['date']} "
                    f"https://www.flylevel.com/Flight/Select?culture=es-ES&triptype=OW&o1=EZE&d1=BCN&dd1={price_info['date']}&ADT=1&CHD=0&INL=0&r=false&mm=false&forcedCurrency=USD&forcedCulture=es-ES&newecom=true&currency=USD"
                )
                send_telegram_message(message, telegram_token, telegram_chat_id)
    else:
        print("No se encontraron precios válidos")

main()