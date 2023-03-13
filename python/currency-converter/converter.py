import os
import sys
from datetime import date
import requests
import time
import json

ratios_file = "ratios.json"


# get_currency_ratio returns exchange as dict or empty dict if it failed to get it
def get_currency_ratio(base_currency, target_currency, tries=4):
    url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}"
    for i in range(tries):
        try:
            response_json_output = requests.get(url).json()
            if response_json_output['success']:
                if response_json_output['info']['rate'] is None:
                    response_json_output['info']['rate'] = 0
                return {
                    "base_currency": response_json_output['query']['from'],
                    "target_currency": response_json_output['query']['to'],
                    "date_fetched": response_json_output['date'],
                    "ratio": response_json_output['info']['rate']
                }
        except:
            pass
            print(f"Connection {i + 1} failure")  # Probably connection failure, alternativelly API could be changed
        time.sleep((i % (tries - 1)) / tries)  # The next enquiry should be a bit later
    print("Failed to get currency from internet")
    return {}


def dump_json_to_file(data, ratios=ratios_file):
    file = open(ratios, "w")
    # print("Writing in file")
    json.dump(data, file, indent=4)
    file.close()


def change_exchange_in_ratios(base_currency, target_currency, exchange, data):
    if exchange["date_fetched"] == str(date.today()):
        return exchange["ratio"]
    new_exchange = get_currency_ratio(base_currency, target_currency)
    if new_exchange == {}:
        return 0
    exchange.update(new_exchange)
    dump_json_to_file(data)
    return new_exchange["ratio"]


def convert_currency(base_currency, target_currency, amount=1):
    ratios = None
    data = None
    if not os.path.isfile(ratios_file):
        dump_json_to_file([])
    for i in range(2):
        try:
            ratios = open(ratios_file, "r")
            try:
                data = json.load(ratios)
            except:
                print("Problem with JSON structure")
                return 0
            break
        except:
            ratios.close()
            dump_json_to_file([]) #The file is probably deleted, this is creating new one
            if i == 1:
                print("Problem with opening file")
                return 0
        ratios.close()


    for exchange in data:
        if base_currency == exchange["base_currency"] and target_currency == exchange["target_currency"]:
            return amount * change_exchange_in_ratios(base_currency, target_currency, exchange, data)
        # I assume the ratio between currecies is an invers (PLN->EUR_ratio == 1 / EUR->PLN_ratio) if this is wrong the 3 lines below can be deleted
        if base_currency == exchange["target_currency"] and target_currency == exchange["base_currency"]:
            ratio = change_exchange_in_ratios(base_currency, target_currency, exchange, data)
            return amount/ratio if ratio != 0 else 0
    new_exchange = get_currency_ratio(base_currency, target_currency)
    if new_exchange == {}:
        return 0
    data.append(new_exchange)
    dump_json_to_file(data)
    return amount * new_exchange["ratio"]


if __name__ == "__main__" and len(sys.argv) == 4:
    converted_amount = 0
    try:
        converted_amount = convert_currency(sys.argv[2], sys.argv[3], float(sys.argv[1]))
    except:
        pass
    print(f"{sys.argv[1]} {sys.argv[2]} = {converted_amount} {sys.argv[3]}")

