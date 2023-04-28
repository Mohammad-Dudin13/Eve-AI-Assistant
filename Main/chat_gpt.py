import openai
import wikipedia


class ChatGPT:
    """
    A class representing a GPT-3.5 chatbot that can generate responses to prompts using the OpenAI API.

    Attributes:
        openai_api_key (str): The API key for accessing the OpenAI API.
        name (str): The name of the chatbot.
        chat_history (list): A list of chat history, consisting of the prompts and responses.

    Methods:
        get_answer(prompt:str,mode:str="assistant") -> str:
            Generates a response to the prompt using the OpenAI API.
        web_searcher(prompt:str) -> str:
            Searches Wikipedia for a summary of the given prompt.
    """

    def __init__(self, name: str, api_key: str):
        """
        Initializes a new instance of the ChatGPT class.

        Args:
            name (str): The name of the chatbot.
            api_key (str): The API key for accessing the OpenAI API.
        """
        self.openai_api_key = api_key
        self.name = name
        self.chat_history = []

    def get_answer(self, prompt: str, mode: str = "assistant") -> str:
        """
        Generates a response to the prompt using the OpenAI API.

        Args:
            prompt (str): The prompt to generate a response to.
            mode (str): The mode of the response generation. Possible values are "assistant" (for generating
                a complete and informative response) and "short" (for generating a short response within 25 words).

        Returns:
            str: The generated response.
        """
        if mode == "assistant":
            self.system_message = f"""
                            Your name is {self.name}, you are a female ai assistant, be respectful and provide short answers
                            """
            self.token_limit = 1000
        elif mode == "short":
            self.system_message = f"""
                            rephrase prompt and provide answer within 50 words
                            """
            self.token_limit = 100

        openai.api_key = self.openai_api_key
        user_prompt = {"role": "user", "content": prompt}
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=self.token_limit,
            messages=[
                {"role": "system",
                 "content": self.system_message},
                *self.chat_history,
                user_prompt,
            ],
        )
        content = response["choices"][0]["message"]["content"]
        self.chat_history.append(user_prompt)
        self.chat_history.append({"role": "assistant", "content": content})
        return content

    @staticmethod
    def web_searcher(prompt: str) -> str:
        """
        Searches Wikipedia for a summary of the given prompt.

        Args:
            prompt (str): The prompt to search on Wikipedia.

        Returns:
            str: The summary of the prompt from Wikipedia.
        """
        return wikipedia.summary(prompt)
