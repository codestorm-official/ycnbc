import ycnbc
import os
import json
import logging
from ycnbc.news.uri import _NEWS_URI_

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

OUTPUT_DIR = "results_test"

def save_output(category: str, data: dict, prefix: str = ""):
    """Saves the provided data to a JSON file."""
    if not data:
        logging.warning(f"No data returned for {category}, skipping save.")
        return

    filename = f"{prefix}{category.replace(' ', '_').replace('/', '_')}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Saved {category} data to {filepath}")
    except Exception as e:
        logging.error(f"Error saving {category} data to {filepath}: {e}")

def run_and_save_all(instance, method_names: list, file_prefix: str):
    """
    Dynamically calls a list of methods on an instance and saves the output.
    """
    logging.info(f"--- Fetching {file_prefix.strip()} data ---")
    for method_name in method_names:
        try:
            logging.info(f"Fetching {method_name}...")
            method = getattr(instance, method_name)
            data = method()
            save_output(method_name, data, prefix=file_prefix)
        except Exception as e:
            logging.error(f"Error fetching {method_name}: {e}")

def main():
    """
    Main function to run all manual fetch operations.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    markets = ycnbc.Markets()
    news = ycnbc.News()

    # --- MARKETS ---
    # Handle methods with arguments separately
    try:
        logging.info("Fetching quote_summary for AAPL...")
        quote_data = markets.quote_summary('AAPL')
        save_output("quote_summary_AAPL", quote_data, prefix="Markets - ")
    except Exception as e:
        logging.error(f"Error fetching quote_summary: {e}")

    # List of market methods without arguments
    market_methods = [
        'pre_markets', 'us_markets', 'europe_markets', 'asia_markets',
        'currencies', 'cryptocurrencies', 'futures_and_commodities',
        'bonds', 'funds_and_etfs'
    ]
    run_and_save_all(markets, market_methods, "Markets - ")

    # --- NEWS ---
    # Generate method names dynamically from the URI config file for simplicity and robustness
    news_methods = [key.replace('-', '_') for key in _NEWS_URI_.keys()]
    run_and_save_all(news, news_methods, "News - ")

    logging.info("--- Manual run complete. ---")

if __name__ == "__main__":
    main()