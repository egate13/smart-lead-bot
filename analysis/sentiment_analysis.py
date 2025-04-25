from transformers import pipeline

# Utilisation du pipeline de transformers pour l'analyse de sentiment
def analyze_sentiment(texts):
    sentiment_analyzer = pipeline("sentiment-analysis")
    
    sentiments = []
    for text in texts:
        result = sentiment_analyzer(text)
        sentiments.append(result[0]['label'])
    
    return sentiments
