import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import random
from keras.models import load_model

class ChatBot:
    """
    A class to represent a chatbot.

    Attributes:
    -----------
    data : dict
        A dictionary containing the data from the intents file.
    tokenizer : keras.preprocessing.text.Tokenizer
        A tokenizer to convert text into numerical sequences.
    label_encoder : sklearn.preprocessing.LabelEncoder
        An encoder to encode target labels into numerical form.
    model : keras.engine.functional.Functional
        A trained model to predict intents.
    training_data : list
        A list containing training patterns.
    output_data : list
        A list containing target labels.
    tags : list
        A list containing unique tags from intents file.

    Methods:
    --------
    _prepare_data():
        Prepares the training and target data using the patterns and tags from the intents file.
    predict_intent(text):
        Predicts the intent of the given text using the trained model.
    generate_response(user_input):
        Generates a random response for the predicted intent.
    """

    def __init__(self, intents_file_path, model_file_path):
        """
        Initializes the `ChatBot` object.

        Parameters:
        -----------
        intents_file_path : str
            The file path to the JSON file containing the intents and responses.
        model_file_path : str
            The file path to the trained model file.
        """
        with open(intents_file_path) as file:
            self.data = json.load(file)

        self.tokenizer = keras.preprocessing.text.Tokenizer()
        self.label_encoder = LabelEncoder()
        self.model = load_model(model_file_path)
        self._prepare_data()
        self.tags = [intent['tag'] for intent in self.data['intents']]

    def _prepare_data(self):
        """
        Prepares the training and target data using the patterns and tags from the intents file.
        """
        self.training_data = []
        self.output_data = []
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                self.training_data.append(pattern)
                self.output_data.append(intent['tag'])

        self.tokenizer.fit_on_texts(self.training_data)
        self.training_data = self.tokenizer.texts_to_matrix(self.training_data, mode='binary')
        self.output_data = self.label_encoder.fit_transform(self.output_data)

    def predict_intent(self, text):
        """
        Predicts the intent of the given text using the trained model.

        Parameters:
        -----------
        text : str
            The input text.

        Returns:
        --------
        str or None
            The predicted intent of the text or None if the confidence is less than 0.5.
        """
        text = self.tokenizer.texts_to_matrix([text], mode='binary')
        prediction = self.model.predict(text, verbose=0)[0]
        predicted_class = np.argmax(prediction)
        confidence = prediction[predicted_class]
        if confidence > 0.5:
            tag = self.label_encoder.inverse_transform([predicted_class])[0]
            return tag
        else:
            return None

    def generate_response(self, user_input):
        """
        Generates a random response for the predicted intent.

        Parameters:
        -----------
        user_input : str
            The input text.

        Returns:
        --------
        str
            A random response for the predicted intent.
        """
        predicted_intent = self.predict_intent(user_input)
        if predicted_intent is not None:
            for intent in self.data['intents']:
                if intent['tag'] == predicted_intent:
                    return random.choice(intent['responses'])
