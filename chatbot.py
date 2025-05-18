import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load FAQ data
with open('faq_data.json', 'r') as f:
    faq_data = json.load(f)

questions = [item['question'] for item in faq_data]
answers = [item['answer'] for item in faq_data]

# NLP preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return ' '.join(tokens)

preprocessed_questions = [preprocess(q) for q in questions]

# Vectorize questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)

def get_answer(user_input):
    user_q = preprocess(user_input)
    user_vec = vectorizer.transform([user_q])
    sims = cosine_similarity(user_vec, X)
    idx = sims.argmax()
    if sims[0, idx] < 0.3:
        return "Sorry, I couldn't find an answer to your question."
    return answers[idx]

if __name__ == "__main__":
    print("Welcome to the Computer Store FAQ Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = get_answer(user_input)
        print("Bot:", response) 