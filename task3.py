import random
import nltk
import spacy

# Download NLTK data (only required once)
# nltk.download("punkt")
# nltk.download("wordnet")

#plsss ensure to pip install the libs above before running the code

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Sample responses
responses = {
    "greeting": ["Hello! How can I help you?", "Hi there! How's it going?", "Hey! What can I do for you?"],
    "farewell": ["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "default": ["I'm sorry, I didn't understand that.", "Can you rephrase?", "I'm not sure I follow."],
}

# Keyword-based rules
keywords = {
    "greeting": ["hello", "hi", "hey", "morning", "evening"],
    "farewell": ["bye", "goodbye", "see you", "later"],
    "thanks": ["thank", "thanks", "appreciate", "grateful"],
}

def preprocess(text):
    """Preprocess input text."""
    text = text.lower()
    doc = nlp(text)
    return [token.lemma_ for token in doc]

def classify_input(user_input):
    """Classify user input based on keywords."""
    tokens = preprocess(user_input)
    for intent, words in keywords.items():
        if any(word in tokens for word in words):
            return intent
    return "default"

def generate_response(intent):
    """Generate a response based on intent."""
    return random.choice(responses[intent])

def chatbot():
    """Run the chatbot."""
    print("Chatbot: Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        intent = classify_input(user_input)
        response = generate_response(intent)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
