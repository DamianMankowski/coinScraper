import re
def extract_price_from_information(information, price):
    value = re.findall(r'\b\d+\b',information)
    priceReal = re.findall(r'\b\d+\b',price.replace(' ',''))
    return float(int(priceReal[0])/int(value[0]))