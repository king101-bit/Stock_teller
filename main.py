import requests

# Replace YOUR_API_KEY with your own API access key
API_URL = "https://openexchangerates.org/api/latest.json?app_id=YOUR_API_KEY"

# Prompt the user to input the currency code and amount in USD
currency_code = input("Enter the currency code you want to convert USD to (e.g. EUR, GBP, NGN): ").upper()
usd_amount = float(input("Enter amount in USD: "))

# Make a GET request to the API and get the response
response = requests.get(API_URL)

# Check if the response status code is OK
if response.status_code == 200:
    data = response.json()

    # Check if the specified currency code exists in the data
    if currency_code in data['rates']:
        # Get the exchange rate for the specified currency
        currency_rate = data['rates'][currency_code]

        # Convert USD to the specified currency
        converted_amount = usd_amount * currency_rate
        print(f"{usd_amount:.2f} USD = {converted_amount:.2f} {currency_code}")
    else:
        print(f"The currency code '{currency_code}' is not valid. Please try again.")
else:
    print("Failed to retrieve exchange rates.")
