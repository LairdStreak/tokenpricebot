#!/usr/bin/python3.6
import requests
TOKEN_URL = 'https://wowtokenprices.com/current_prices.json'

def get_token_price():
    ''' Return The current token price from the API Provided'''
    data_response = requests.get(TOKEN_URL)
    jason_data = data_response.json()
    return f"Current Price {jason_data['us']['current_price']}."

def main():
    '''Main function'''
    print(get_token_price())

if __name__ == '__main__':
    main()
