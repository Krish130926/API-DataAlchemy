# Crypto Price & News Aggregator

## Description

This project gathers real-time cryptocurrency price data and the latest crypto news using two sources:

1. **API**: We use the CoinGecko API to fetch the current prices of user-defined cryptocurrencies (e.g., Bitcoin, Ethereum) in a specified currency (USD, EUR, etc.). This allows users to view the most up-to-date pricing information for their crypto assets.
   
2. **Web Scraper**: We scrape the latest news headlines from CoinTelegraph, one of the leading news platforms for cryptocurrency-related updates. The user can specify how many news articles they'd like to view.

### Purpose

- **CoinGecko API**: CoinGecko is a well-established cryptocurrency data aggregator offering free access to price information for thousands of digital assets. It provides reliable, real-time updates, making it an excellent choice for fetching live crypto prices.
  
- **CoinTelegraph**: This site was chosen because it provides extensive coverage on blockchain, cryptocurrency, and fintech developments, ensuring users receive the latest industry news.

### Dataset Value

The dataset provides real-time prices and financial news in a combined format, allowing users to make informed decisions regarding their cryptocurrency investments. This combination of live price data and up-to-date news offers insights that are typically scattered across different platforms, saving users time and effort.

#### Why this dataset is unique:

- **Dynamic data**: Unlike static datasets, this project pulls real-time information. Many datasets available online are historical or outdated.
  
- **Aggregated insights**: The combination of price data and news offers a more comprehensive overview of the crypto market, which is often fragmented across different platforms.
  
- **Customizable**: Users can input the crypto symbol, currency, and number of news articles they want to see, providing tailored outputs.

While individual components of this dataset might be available for free (such as API price data), the aggregation of both real-time price and news information into a single dataset, with user-defined inputs, makes this project particularly valuable. Real-time aggregation like this is often only available via paid services.

## Running the Project

Examples: 

Input:

Enter the cryptocurrency symbol (e.g., bitcoin, ethereum).
Specify the currency for conversion (e.g., usd, eur).
Choose how many news articles to retrieve (e.g., 5).


Output:

The current price of the selected cryptocurrency in the chosen currency.
The top news headlines related to cryptocurrencies.
The data will be saved in a file named crypto_data.csv in the project directory.

Example Output, 
Crypto Symbol, Price (USD), Latest News Headlines
bitcoin, 27000, "Bitcoin price surges after major announcement; Ethereum 2.0 sees record adoption rates"
