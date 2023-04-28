import speech_recognition as sr

class SpeechToText:
    """
    This class is used for speech to text conversion.

    Attributes:
        recognizer (Recobinary interaction parametersgnizer): The speech recognition engine.
        microphone (Microphone): The microphone used to capture the audio input.

    Methods:
        get_text_from_audio(): Uses the microphone to capture audio input, converts it to text
        and returns the text.

    """

    def __init__(self):
        """
        Initializes the SpeechToText object with a speech recognizer and a microphone.
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def get_text_from_audio(self):
        """
        Uses the microphone to capture audio input, converts it to text and returns the text.

        Returns:
            str: The text obtained from the speech input.
        """
        with self.microphone as source:
            # Adjusts for ambient noise to improve recognition accuracy
            self.recognizer.adjust_for_ambient_noise(source, duration=0.1)
            # Listens to the microphone and captures the audio input
            audio = self.recognizer.listen(source)
            # Transcribes the audio input to text using Google's Speech Recognition API
            text = self.recognizer.recognize_google(audio)
            # Converts the text to lowercase to standardize the input
            text = text.lower()
            return text