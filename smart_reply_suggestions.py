import json
import random
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


# Load the intent.json file
with open('intent.json') as file:
    data = json.load(file)

# Create lists to store the data
X = []  # Text data
y = []  # Intent labels

# Extract the text and intent labels from the data
for intent in data['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])

# Convert the text data to numerical form using a CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)


with open('approach_3.pkl', 'rb') as f:
    loaded_classifier = pickle.load(f)

def get_response(text):
    # Convert the text to numerical form using the CountVectorizer
    input_data = vectorizer.transform([text])
    # Use the trained model to predict the intent label for the input data
    predicted_intent_probs = loaded_classifier.predict_proba(input_data)[0]
    # Get the index of the highest probability
    max_prob_index = np.argmax(predicted_intent_probs)
    # Get the predicted intent label and corresponding probability
    predicted_intent = loaded_classifier.classes_[max_prob_index]
    print("Predicted intent --->>", predicted_intent)
    predicted_prob = predicted_intent_probs[max_prob_index]
    print("Prob --->>", predicted_prob)
    # Check if the predicted probability is greater than 0.8
    if predicted_prob >= 0.40:
        # Get a list of responses for the predicted intent label
        responses = []
        for intent in data['intents']:
            if intent['tag'] == predicted_intent:
                responses = intent['responses']
        suggestions = random.sample(responses,3)
        for i, suggestion in enumerate(suggestions):
            suggestions[i] = f"Suggestions {i + 1}: {suggestion}"
        # Choose a random response from the list and return it
        # return random.sample(responses,3)
        return suggestions
    else:
        # Return a default response if the predicted probability is too low
        return ["I'm sorry, I didn't understand that."]
    
print(get_response("no"))

