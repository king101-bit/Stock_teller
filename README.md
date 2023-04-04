# Currency Converter
This Python script fetches the exchange rates for USD and GBP from Open Exchange Rates and converts them to Nigerian Naira (NGN).

<strong>Prerequisites</strong> <br>
To run this code, you will need:

Python 3.x installed on your machine
An API key from Open Exchange Rates. You can sign up for a free account to get an API key.
<strong>Setup</strong>
Clone this repository to your local machine.

Open a terminal window and navigate to the repository directory.

Install the required dependencies by running the following command:

<pre><code>```python
pip install requests
```</code></pre>
Create a file called .env in the project directory and add the following line, replacing YOUR_API_KEY with your Open Exchange Rates API key:


<pre><code>```python
OER_API_KEY=YOUR_API_KEY
```</code></pre>
OER_API_KEY=YOUR_API_KEY
Usage
To run the code, simply execute the following command in your terminal:

<pre><code>```python
python main.py
```</code></pre
The code will fetch the exchange rates for USD and GBP from Open Exchange Rates and convert them to NGN using the current exchange rates. The converted amounts will be displayed in the terminal.

License
This code is licensed under the MIT License. Feel free to use it however you like!
