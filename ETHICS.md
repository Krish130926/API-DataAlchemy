# Ethical Considerations

## 1. Data Privacy & Transparency

The project does not involve gathering any personal data or sensitive user information. The API used (CoinGecko) and the news scraped (CoinTelegraph) provide publicly available data. We ensure that no personally identifiable information (PII) is collected or used, and there is transparency regarding the sources of data.

## 2. API and Web Scraping Ethics

- **Respecting Rate Limits**: We use appropriate rate limiting to avoid overwhelming the CoinGecko API and CoinTelegraph's servers. Our script is designed to retry failed requests with delays, ensuring we respect the API's and website's traffic capacity.
  
- **Respecting Terms of Service**: We have ensured that CoinGecko's API allows free access to the type of data we are gathering. We also adhere to CoinTelegraph's guidelines by limiting the amount of data we scrape and ensuring it is only for educational and non-commercial purposes.

## 3. Data Accuracy and Representation

While we aim to provide real-time data, cryptocurrency prices and news are volatile, and information can change rapidly. We include a disclaimer that the dataset is for informational purposes only and should not be considered financial advice.

## 4. Fair Use of Information

The news content scraped from CoinTelegraph is limited to headlines, which does not infringe on full article content or intellectual property. We encourage users to visit CoinTelegraph for complete articles, respecting the platform's right to distribute its content.

## 5. Legal Compliance

We ensure compliance with the laws regarding web scraping and API usage. The project is strictly for educational purposes, demonstrating how data gathering can be performed using public APIs and web scraping without violating ethical standards.
