#NLP logic to analyze sentiment, extract keywords and summarize text
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

nlp = spacy.load('en_core_web_sm')
stop_words = set(stopwords.words('english') + list(punctuation))


def analyze_sentiment(text):
    doc = nlp(text)
    return "Positive" if doc.cats['POSITIVE'] > 0.5 else "Negative"


def extract_keywords(text):
    words = nltk.word_tokenize(text)
    keywords = [word for word in words if word.lower() not in stop_words]
    return ', '.join(set(keywords))


def summarize_text(text):
    doc = nlp(text)
    summary = list(doc.sents)[0] if len(doc.sents) > 0 else ""
    return str(summary)
