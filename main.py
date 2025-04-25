from scraper.reddit_scraper import scrape_reddit
from analysis.sentiment_analysis import analyze_sentiment

def main():
    # Exemple de scraping de Reddit
    print("Scraping Reddit...")
    data = scrape_reddit(query="besoin de conseils pour dropshipping")
    
    # Analyse de sentiments des messages
    print("Analyse des sentiments...")
    sentiments = analyze_sentiment(data)

    print(f"Sentiment analyse: {sentiments}")

if __name__ == "__main__":
    main()
