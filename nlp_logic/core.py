from textblob import TextBlob
import wikipedia


def search_wiki(key):
    print(f'Searchin for: {key}')
    return wikipedia.search(key)


def summerize_wiki(name):
    print(f'Searching Wikipedia Summary for: {name}')
    return wikipedia.summary(name)


def get_blob(text):
    return TextBlob(text)


def get_phrases(name):
    text = summerize_wiki(name)
    blob = get_blob(text)
    return blob.noun_phrases



