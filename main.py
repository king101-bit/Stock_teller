import requests

# Replace YOUR_APP_ID with your own API access key
API_URL = "https://openexchangerates.org/api/latest.json?app_id=0314b9a2e7f043b1886ff9648cbf116a"

# Make a GET request to the API and get the response
response = requests.get(API_URL)

# If the response status code is OK, parse the response JSON data
if response.status_code == 200:
    data = response.json()

    # Get the exchange rates for USD and GBP
    usd_rate = data['rates']['USD']
    gbp_rate = data['rates']['GBP']
    ngn_rate = data['rates']['NGN']

    # Print the exchange rates
    print(f"1 USD = ₦{ngn_rate/usd_rate:.2f}")
    print(f"1 GBP = ₦{ngn_rate/gbp_rate:.2f}")
else:
    print("Failed to retrieve exchange rates.")
