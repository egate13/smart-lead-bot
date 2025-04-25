import streamlit as st
from scraper.reddit_scraper import scrape_reddit
from analysis.sentiment_analysis import analyze_sentiment

def app():
    st.title("Smart Lead Bot - Dashboard")
    
    query = st.text_input("Entrez une recherche Reddit", "besoin de conseils pour dropshipping")
    if query:
        data = scrape_reddit(query)
        sentiments = analyze_sentiment(data)
        
        st.write(f"Résultats de recherche pour : {query}")
        st.write(data)
        
        st.write("Analyse des sentiments")
        st.write(sentiments)

if __name__ == "__main__":
    app()
