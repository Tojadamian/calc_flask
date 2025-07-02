import requests

NBP_TAB = ['a', 'b', 'c']

def get_all_currencies_code():
    codes = set()
    for tab in NBP_TAB:
        url = f'http://api.nbp.pl/api/exchangerates/tables/{tab}/?format=json'
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            for rate in data[0]['rates']:
                codes.add(rate['code'])
    return sorted(codes)

def get_exchange_rate(code):
    if code.upper() == 'PLN':
        return 1.0
    tables = find_currency_table(code)
    if not tables:
        return None
    tab = tables[0].lower()
    url = f'http://api.nbp.pl/api/exchangerates/rates/{tab}/{code}/?format=json'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        if tab in ['a', 'b']:
            return data['rates'][0]['mid']
        elif tab == 'c':
            return data['rates'][0]['bid'], data['rates'][0]['ask']
    return None

def find_currency_table(currency_code):
    found_tables = []
    for tab in NBP_TAB:
        url = f'http://api.nbp.pl/api/exchangerates/tables/{tab}/?format=json'
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            for rate in data[0]['rates']:
                if rate['code'].upper() == currency_code.upper():
                    found_tables.append(tab)
            # print(f"Found {len(found_tables)} tables for currency {currency_code}: {found_tables}")
    return found_tables

def convert_currency(amount, from_code, to_code):
    from_rate = get_exchange_rate(from_code)
    to_rate = get_exchange_rate(to_code)
    if from_rate is None or to_rate is None:
        return None
    return (amount * from_rate) / to_rate

# print(find_currency_table('JOD'))  # Example usage, you can remove this line later
# print(get_exchange_rate('USD'))  # Example usage, you can remove this line later
# print(convert_currency(100, 'USD', 'EUR'))  # Example usage, you can remove this line later