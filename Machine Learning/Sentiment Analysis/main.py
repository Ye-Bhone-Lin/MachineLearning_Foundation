import streamlit as st 
import re
from hashlib import new
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')# for tokenization
nltk.download('omw-1.4') #for wordnet
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

text_input = st.text_input("Sentiment Analysis")

def cleaning_text(text):
    return re.sub("[^A-Za-z]", " ", text)

clean_text = cleaning_text(text_input)

pos_dict = {"J":wordnet.ADJ, "N":wordnet.NOUN, "V":wordnet.VERB, "R":wordnet.ADV}
def token_pos_stop(text):
    tags = pos_tag(word_tokenize(text))
    new_list = []
    for word , tag in tags:
        if word.lower() not in set(stopwords.words("english")):
            new_list.append(tuple([word,pos_dict.get(tag[0])]))
    return new_list 

pos_text = token_pos_stop(clean_text)


def lemmetize(pos_words):
    word_net= WordNetLemmatizer()

    lemme_new = " "
    for word, tag in pos_words:
        if not tag:
            lemma = word
            lemme_new = lemme_new + " " + lemma
        else:
            lemma = word_net.lemmatize(word, pos=tag)
            lemme_new = lemme_new + " " + lemma
    return lemme_new

stem_text = lemmetize(pos_text)

def  subjectivity_score(review):
    return TextBlob(review).sentiment.subjectivity

def polarity_score(review):
    return TextBlob(review).sentiment.polarity

def analysis(Score):
    if Score < 0:
        return "Negative"
    elif Score == 0:
        return "Neutral"
    else:
        return "Postive"

sentiment_analysis = polarity_score(stem_text)
st.write(analysis(sentiment_analysis))