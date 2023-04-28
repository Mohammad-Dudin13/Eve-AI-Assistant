from speech_to_text import SpeechToText
from chat_gpt import ChatGPT
from text_to_speech import TextToSpeech
from microphone_muter import MicrophoneMute
from model_application import ChatBot
from movies import MovieRecommendation
import tkinter as tk
from gif_animation import ImageLabel
import continuous_threading
import requests
from bs4 import BeautifulSoup
import datetime

continuous_threading.set_allow_shutdown(True)


class Assistant:
    """
       The main assistant class that handles the user input and generates appropriate responses.
       """
    def __init__(self, name, gpt_token):
        """
        Constructor method for the AIAssistant class.

        Args:
            name (str): The name of the AI assistant.
            gpt_token (str): The API token for GPT-3 OpenAI.

        Returns:
            None
        """
        # Assigns the name and API token to the instance variables
        self.name = name
        self.gpt_token = gpt_token

        # Initializes objects for speech-to-text conversion, GPT-3 chatbot, text-to-speech conversion, and microphone control
        self.speech_to_text = SpeechToText()
        self.chat_gpt = ChatGPT(name, gpt_token)
        self.text_to_speech = TextToSpeech()
        self.microphone_mute = MicrophoneMute()

        # Initializes the chatbot and retrieves the possible tags for responses
        self.chatbot = ChatBot('intents.json', 'chatbot1.h5')
        self.tags = self.chatbot.tags

        # Initializes the movie recommendation system
        self.movie_recommender = MovieRecommendation()

        # Initializes the Tkinter GUI window and loads the GIF animation for the UI
        self.root = tk.Tk()
        self.root.title(f"{self.name} AI Assistant")
        self.root.resizable(False, False)
        self.label = ImageLabel(self.root)
        self.label.pack(fill="both", expand=True)
        self.gif_file = "animation.gif"
        self.label.load(self.gif_file)

        # Runs the assistant in a continuous thread for handling user inputs and outputs
        self.root.after(1, continuous_threading.Thread(target=self.run).start())
        self.root.mainloop()

    def get_current_time(self):
        """
        Retrieves the current time from the local machine.

        Returns:
            str: The current time in HH:MM format.
        """
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return current_time

    def run(self):
        """
        This method runs the chatbot and controls its interaction with the user.

        It starts by unmuting the microphone, then listens for the user's input using speech-to-text conversion.
        The chatbot then predicts the user's intent and responds accordingly.
        If the user's intent is "general", the chatbot uses GPT-3 API to generate a response.
        Otherwise, it uses specific functionalities for each intent, such as recommending a movie or searching the web.
        The chatbot will continue to interact with the user until the user indicates the intent to leave the conversation.
        At that point, the chatbot will mute the microphone, say goodbye, and shut down.

        Args:
            self: the instance of the `ChatbotGUI` class calling this method.

        Returns:
            None
        """
        # Unmute microphone to listen for user input
        self.microphone_mute.unmute_microphone()

        # Continuously listen for user input and generate responses until the chatbot is terminated
        while True:
            try:
                # Convert audio input to text and predict intent of input
                text = self.speech_to_text.get_text_from_audio()
                intent = self.chatbot.predict_intent(text)

                # If the intent is not 'general', generate a response based on the specific intent
                if intent !="general":
                    answer = self.chatbot.generate_response(text)

                    # If the intent is 'goodbye', terminate the application
                    if intent == "goodbye":
                        # Print user input and response, mute the microphone, play the response aloud,
                        # and terminate the application
                        self.print_multiline(f"You :> {text}")
                        self.microphone_mute.mute_microphone()
                        self.print_multiline(f"{self.name} :> {answer}")
                        self.text_to_speech.play_audio(answer)
                        continuous_threading.set_shutdown_timeout(0)
                        self.root.destroy()
                        break

                    # If the intent is "time", retrieve the current time and generate the response
                    elif intent == "time":
                        current_time = self.get_current_time()
                        answer = f"The current time is {current_time}."
                        # Print and play the response aloud
                        self.print_multiline(f"You :> {text}")
                        self.microphone_mute.mute_microphone()
                        self.print_multiline(f"{self.name} :> {answer}")
                        self.text_to_speech.play_audio(answer)
                        self.microphone_mute.unmute_microphone()
                        continue

                    # If the intent is 'greetings', prompt the user to respond and continue listening for input
                    elif intent == "greetings":
                        # Print user input and response, mute the microphone, play the response aloud,
                        # and continue listening for input
                        self.print_multiline(f"You :> {text}")
                        self.microphone_mute.mute_microphone()
                        self.print_multiline(f"{self.name} :> {answer}")
                        self.text_to_speech.play_audio(answer)
                        self.microphone_mute.unmute_microphone()
                        continue

                    # If the intent is 'movie suggestion', prompt the user to input genre, year, and rating criteria,
                    # and generate a movie recommendation based on the criteria
                    elif intent == "movie suggestion":
                        # Print user input and response, mute the microphone, play the response aloud, and prompt
                        # the user to input genre, year, and rating criteria
                        self.print_multiline(f"You :> {text}")
                        self.microphone_mute.mute_microphone()
                        self.print_multiline(f"{self.name} :> {answer}")
                        self.text_to_speech.play_audio(answer)
                        print(f"Input without brackets in the same order (Genre, Year, Rating) :")
                        text2 = input()
                        text2_tokenized = text2.split(',')
                        self.microphone_mute.mute_microphone()
                        answer2 = self.movie_recommender.recommend_movie(genre=text2_tokenized[0],
                                                                         min_rating=float(text2_tokenized[2]),
                                                                         year=int(text2_tokenized[1]))
                        print(f"{self.name} :> {self.movie_recommender.stringer(answer2)}")
                        self.text_to_speech.play_audio(str(self.movie_recommender.recommendation_lst_shorter(answer2)))
                        self.microphone_mute.unmute_microphone()
                        continue

                    elif intent == "weather":
                        # Retrieve the weather information using the get_weather method
                        # Print and play the response aloud
                        print(f"You :> {text}")
                        self.microphone_mute.mute_microphone()
                        self.print_multiline(f"{self.name} :> {answer}")
                        self.text_to_speech.play_audio(answer)
                        print(f"Type the City : ")
                        text2 = input()
                        weather_info = self.get_weather(text2)
                        self.print_multiline(f"{self.name} :> {weather_info}")
                        self.text_to_speech.play_audio(weather_info)
                        self.microphone_mute.unmute_microphone()
                        continue

                    # If the intent is 'search web', prompt the user to input a topic to search the web about,
                    # generate a short answer based on the topic, and play the answer aloud
                    elif intent == "search web":
                        # Print user input and response, mute the microphone, play the response aloud,
                        # and prompt the user to input the topic to search for on the web
                        self.print_multiline(f"You :> {text}")
                        self.microphone_mute.mute_microphone()
                        self.print_multiline(f"{self.name} :> {answer}")
                        self.text_to_speech.play_audio(answer)
                        print("Insert the Topic You Want to Search the Web About (the Info is Retrieved from Wikipedia): ")
                        text2 = input()
                        # Use the chatbot's GPT-3 model to summarize the resulted Wikipedia Search to the topic
                        # then print and play the response aloud
                        answer2 = self.chat_gpt.get_answer(
                            f"summarize in no more than 50 words: {self.chat_gpt.web_searcher(text2)}",
                            mode="short")
                        self.print_multiline(f"{self.name} :> {answer2}")
                        self.text_to_speech.play_audio(answer2)
                        self.microphone_mute.unmute_microphone()
                        continue

                else:
                    # Print user input, get GPT-3 response, mute the microphone,
                    # play response aloud or just returns it if the user don't want for the assistant to play it,
                    # and unmute the microphone
                    self.print_multiline(f"You :> {text}")
                    answer = self.chat_gpt.get_answer(text)
                    self.microphone_mute.mute_microphone()
                    print(f"Do You Want {self.name} to say it? (Y/n) ")
                    print_or_listen = input()
                    self.print_multiline(f"{self.name} :> {answer}")
                    if print_or_listen.lower() == 'n':
                        self.microphone_mute.unmute_microphone()
                    else:
                        self.text_to_speech.play_audio(answer)
                        self.microphone_mute.unmute_microphone()
                    continue
            except:
                # if any error occur during microphone listening, continue the while loop until you get an input
                continue
    @staticmethod
    def get_weather(city):
        city = city + " weather"
        city = city.replace(" ", "+")
        url = f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        params = {
            'hl': 'en'  # Set the language parameter to 'en' for English results
        }
        res = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        lst = ["on " + time[:-3] + " " + time[-2:],
               f'the Weather in {city[:-8].title()} is ' + info,
               "With a Temperature of " + weather + "°C"]
        string = ", ".join(lst)
        return string
    @staticmethod
    def print_multiline(string, width=50):
        """
                Method to print a string in multiple lines if with a given width (defaulted at 50 words).

                Args:
                    string (str): The string to be printed.
                    width (int): The maximum width of each line.

                Returns:
                    None
                """
        words = string.split()
        line = ""
        for word in words:
            if len(line + " " + word) > width and line[-1] in [",",".","?","!"]:
                print(line)
                line = word
            else:
                line += " " + word
        print(line)
