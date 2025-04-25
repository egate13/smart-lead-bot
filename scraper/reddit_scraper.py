import praw
import snscrape.modules.reddit as sreddit

# Utiliser praw (nécessite une API Reddit)
def scrape_reddit_praw(query):
    reddit = praw.Reddit(client_id='your-client-id', client_secret='your-client-secret', user_agent='your-user-agent')
    results = reddit.subreddit('all').search(query, limit=10)
    
    return [result.title for result in results]

# Utiliser snscrape (sans API)
def scrape_reddit_snscrape(query):
    scraper = sreddit.RedditSearchScraper(query)
    results = scraper.get_items()
    return [item.content for item in results]

def scrape_reddit(query, use_praw=True):
    if use_praw:
        return scrape_reddit_praw(query)
    else:
        return scrape_reddit_snscrape(query)
