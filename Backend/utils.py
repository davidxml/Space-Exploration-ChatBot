import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string

# Ensure neccessary NLTK data is downloaded 
nltk.download ('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def preprocess_text(text):
    """
    Tokenizes, lowercases, removes punctuation, and lemmatizes input text.add
    Returns a list of clean tokens. 
    """
    # initializes lemmatizer 
    lemmatizer = WordNetLemmatizer()

    # Step 1: Tokenize 
    tokens = nltk.word_tokenize(text)

    # Step 2: Lowercase
    tokens = [token.lower() for token in tokens]

    # Step 3: Remove Punctuation
    tokens = [token for token in tokens if token not in string.punctuation]

    # Step 4: POS (Part of speech) tagging 
    pos_tags = nltk.pos_tag(tokens)

    # Steps 5: Lemmatize based on POS
    def get_wordnet_pos(tag):
        """
        Convert POS tag to format recognized by WordNetLemmatizer
        """
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN    # default
    
    lemmatized_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]

    return lemmatized_tokens

    print(preprocess_text("The dogs are barking"))