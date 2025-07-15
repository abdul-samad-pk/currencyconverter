from dotenv import load_dotenv
import os
import requests
from num2words import num2words

load_dotenv()  # Load variables from .env


class CurrencyConverter:
    """
    Currency Converter Script

    This script converts one currency to another using real-time exchange rates from currencyapi.com.
    It also spells out the converted amount using the num2words library.

    Author: Abdul Samad
    """

    def __init__(self):
        self.parameters = None
        self.url = 'https://api.currencyapi.com/v3/latest'
        self.api_key = os.getenv("CURRENCY_API_KEY")
        self.ask_first = ""
        self.ask_second = ""
        self.ask_for_currency()
        self.sending_requests()

    def ask_for_currency(self):
        self.ask_first = input("First currency?: ").upper()
        self.ask_second = input("Second currency?: ").upper()

    def sending_requests(self):
        self.parameters = {
            "apikey": self.api_key,
            "base_currency": f"{self.ask_first}"
        }

        response = requests.get(self.url, params=self.parameters)
        data = response.json()

        try:
            rate = data['data'][self.ask_second]['value']
        except KeyError:
            print("Invalid currency code entered or data not available.")
            return

        print(f"Current Rate from {self.ask_first} to {self.ask_second}: {rate}")
        ask_amount = int(input("How many units do you want to convert? "))
        converted_amount = round(rate * ask_amount, 2)
        print(f"Converted amount: {converted_amount}")
        print(num2words(converted_amount).capitalize())


if __name__ == "__main__":
    CurrencyConverter()
