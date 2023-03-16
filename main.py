import requests

# Replace YOUR_APP_ID with your own API access key
API_URL = "https://openexchangerates.org/api/latest.json?app_id=YOUR_API_KEY"

# Make a GET request to the API and get the response
response = requests.get(API_URL)

# If the response status code is OK, parse the response JSON data
if response.status_code == 200:
    data = response.json()

    # Get the exchange rate for NGN
    ngn_rate = data['rates']['NGN']

    # Prompt the user to input an amount in USD
    usd_amount = float(input("Enter amount in USD: "))

    # Convert USD to NGN and print the result
    ngn_amount = usd_amount * ngn_rate
    print(f"{usd_amount:.2f} USD = ₦{ngn_amount:.2f}")
else:
    print("Failed to retrieve exchange rates.")
