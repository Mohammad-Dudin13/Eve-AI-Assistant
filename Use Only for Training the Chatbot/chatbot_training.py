import json
import numpy as np
from tensorflow import keras
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from sklearn.preprocessing import LabelEncoder
import random

# Load the data from the JSON file
with open('intents.json') as file:
    data = json.load(file)

# Create lists to store the training data and output data
training_data = []
output_data = []

# Loop through the intents and their patterns to create training data
for intent in data['intents']:
    for pattern in intent['patterns']:
        training_data.append(pattern)
        output_data.append(intent['tag'])

# Tokenize the training data and convert to binary matrix
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(training_data)
training_data = tokenizer.texts_to_matrix(training_data, mode='binary')

# Encode the output data
label_encoder = LabelEncoder()
output_data = label_encoder.fit_transform(output_data)

# Define the neural network architecture
model = keras.models.Sequential()
model.add(Dense(128, input_shape=(training_data.shape[1],), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(np.max(output_data)+1, activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer=SGD(lr=0.01), metrics=['accuracy'])

# Train the model
chatbot_model = model.fit(training_data, output_data, epochs=1000, batch_size=5)

# Save the model to a file
model.save("chatbot1.h5",chatbot_model)

# Now that the model is trained, you can use it to make predictions:

def predict_intent(text):
    # Tokenize and convert to binary matrix
    text = tokenizer.texts_to_matrix([text], mode='binary')
    # Make prediction using the trained model
    prediction = model.predict(text)[0]
    predicted_class = np.argmax(prediction)
    confidence = prediction[predicted_class]
    if confidence > 0.5:
        # Inverse transform to get the predicted tag
        tag = label_encoder.inverse_transform([predicted_class])[0]
        return tag
    else:
        return None

# Example usage:
user_input = "time"
predicted_intent = predict_intent(user_input)
print(predicted_intent)
for intent in data['intents']:
    if intent['tag'] == predicted_intent:
        print(random.choice(intent['responses']))
