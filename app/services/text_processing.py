#NLP logic to analyze sentiment, extract keywords and summarize text
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from string import punctuation

# If it's the first time you're running this code, you'll need to download the 'vader_lexicon', 'stopwords' and
# 'en_core_web_sm', so uncomment the following lines:
# nltk.download('popular')
# nltk.download('vader_lexicon')
# nltk.download('stopwords')
# spacy.cli.download("en_core_web_sm")

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english') + list(punctuation))


def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    return "Positive" if score['compound'] >= 0.05 else ("Negative" if score['compound'] <= -0.05 else "Neutral")


def extract_keywords(text):
    words = nltk.word_tokenize(text)
    keywords = [word for word in words if word.lower() not in stop_words]
    return ', '.join(set(keywords))


def summarize_text(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    return str(sentences[0]) if sentences else ""
