import requests
import csv
import time

# Your NewsAPI key
NEWS_API_KEY = 'b4a53e8d98cd4876b54f4ba366d961ca'

# Function to fetch cryptocurrency prices using CoinGecko API with error handling
def fetch_crypto_prices(crypto_symbol, currency):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies={currency}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        price = data.get(crypto_symbol, {}).get(currency, 'N/A')
        print(f"The current price of {crypto_symbol} is: {price} {currency.upper()}")
        return price
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch crypto prices: {e}")
        return None

# Function to fetch the latest news from NewsAPI with error handling
def fetch_crypto_news(news_limit, keyword=None):
    query = f"cryptocurrency" if not keyword else keyword
    news_url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={news_limit}&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(news_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        articles = data.get("articles", [])
        headlines = [article['title'] for article in articles]

        print(f"\nLatest Crypto News (showing top {news_limit} articles for '{query}'):")
        for i, headline in enumerate(headlines[:news_limit], 1):  # Print based on user limit
            print(f"{i}. {headline}")
        return headlines[:news_limit]
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch news: {e}")
        return None

# Rate limiter function to avoid overwhelming the API
def rate_limited_request(func, *args, retries=3, delay=2):
    for attempt in range(retries):
        result = func(*args)
        if result:
            return result
        else:
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
    print("Max retries reached, request failed.")
    return None

# Save the fetched data to a CSV file
def save_to_csv(crypto_symbol, price, currency, news_headlines):
    with open('crypto_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Crypto Symbol", f"Price ({currency.upper()})", "Latest News Headlines"])
        writer.writerow([crypto_symbol, price, "; ".join(news_headlines)])
    print("Data saved to crypto_data.csv")

# Main function
if __name__ == "__main__":
    # Take user input for the cryptocurrency symbol and currency
    crypto_symbol = input("Enter the cryptocurrency symbol (e.g., bitcoin, ethereum): ").lower()
    currency = input("Enter the currency for conversion (e.g., usd, eur): ").lower()

    # Take user input for the number of news articles to fetch
    news_limit = int(input("Enter the number of news articles you want to see (e.g., 5): "))
    
    # Take user input for keywords to filter news articles
    keyword = input("Enter a keyword to filter news articles (or press Enter for all): ").strip() or None

    # Fetch crypto price with rate limiting and error handling
    price = rate_limited_request(fetch_crypto_prices, crypto_symbol, currency)

    # Fetch the latest news with rate limiting and error handling
    news_headlines = rate_limited_request(fetch_crypto_news, news_limit, keyword)

    # If both data gathering processes succeed, save to CSV
    if price and news_headlines:
        save_to_csv(crypto_symbol, price, currency, news_headlines)
