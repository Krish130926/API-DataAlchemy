import requests
from bs4 import BeautifulSoup
import time
import csv

# Function to fetch cryptocurrency prices using CoinGecko API with error handling
def fetch_crypto_prices(crypto_symbol):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        price = data.get(crypto_symbol, {}).get('usd', 'N/A')
        print(f"The current price of {crypto_symbol} is: ${price}")
        return price
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch crypto prices: {e}")
        return None

# Function to scrape the latest news from CoinTelegraph with error handling
def scrape_crypto_news():
    news_url = "https://cointelegraph.com/tags/cryptocurrencies"
    try:
        page = requests.get(news_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Extract the headlines (example: headlines within <h2> tags)
        headlines = [headline.text for headline in soup.find_all('h2', class_='post-card-inline__title')]
        
        print("\nLatest Crypto News:")
        for i, headline in enumerate(headlines[:5], 1):  # Print top 5 headlines
            print(f"{i}. {headline}")
        return headlines[:5]  # Return top 5 headlines
    except Exception as e:
        print(f"Failed to scrape news: {e}")
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
def save_to_csv(crypto_symbol, price, news_headlines):
    with open('crypto_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Crypto Symbol", "Price (USD)", "Latest News Headlines"])
        writer.writerow([crypto_symbol, price, "; ".join(news_headlines)])
    print("Data saved to crypto_data.csv")

# Main function
if __name__ == "__main__":
    # Take user input for the cryptocurrency symbol
    crypto_symbol = input("Enter the cryptocurrency symbol (e.g., bitcoin, ethereum): ").lower()

    # Fetch crypto price with rate limiting and error handling
    price = rate_limited_request(fetch_crypto_prices, crypto_symbol)
    
    # Scrape latest news with error handling
    news_headlines = rate_limited_request(scrape_crypto_news)

    # If both data gathering processes succeed, save to CSV
    if price and news_headlines:
        save_to_csv(crypto_symbol, price, news_headlines)
