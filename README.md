# Currency Converter (Python OOP)

A simple and interactive currency converter built using Python and object-oriented programming.  
It fetches real-time exchange rates from (https://currencyapi.com) and spells out the converted amount using the `num2words` library.

### 💡 Features:
- Real-time currency conversion using currencyapi.com
- Input base and target currency interactively
- Amount converted shown in both number and words
- Secure API key handling using `.env` file

### 📦 Technologies:
- Python 3
- requests
- num2words
- python-dotenv

### ▶️ How to Run:
```bash
pip install requests num2words python-dotenv
python currency_converter.py
````

### 🔐 Setup `.env` file:

Create a `.env` file in the project directory with this line:

```
CURRENCY_API_KEY=your_real_api_key_here
```

### 📝 Example:

```
First currency?: USD
Second currency?: PKR
Current Rate from USD to PKR: 278.5
How many units do you want to convert? 5
Converted amount: 1392.5
One thousand, three hundred and ninety-two point five

---
