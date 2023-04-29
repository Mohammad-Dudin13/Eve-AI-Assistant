# Eve-AI-Assistant
Eve is a Python-based AI assistant that utilizes a trained chatbot, **TensorFlow**, and **OpenAI** API. It offers various functionalities, including movie recommendations from IMDb, web searching via Wikipedia, and retrieving weather information for specified cities. For complex tasks like writing poems, emails, and coding, Eve leverages the power of OpenAI's API (user key required). Users communicate with Eve by providing prompts through speech, which are converted to text for processing. The generated responses are then transformed back into speech using the gTTS (Google Text-to-Speech) model, enabling a seamless and interactive user experience.

## Features
* **Movie recommendations**: Eve can suggest movies based on genre, year, and minimum rating using data from IMDb.
* **Web searching**: Utilizing Wikipedia, Eve can search the web and provide short summaries on various topics.
* **Weather information**: Users can request weather details for specified cities, which Eve retrieves using relevant APIs.
* **Complex tasks**: For advanced tasks like writing poems, emails, and coding, Eve utilizes OpenAI's API (user key required).

## Installation and Running
To execute the program, ensure that **Python 3.10** or a higher version is installed on your system. Please follow the steps below to install and run Eve via the Terminal:
1. Clone the repository:
```terminal
git clone https://github.com/Xecutioner13/Eve-AI-Assistant
```
2. Navigate to the project directory:
```terminal
cd Eve-AI-Assistant
```
3. Install the required dependencies:
```terminal
pip install -r requirements.txt
```
4. Open the main.py file located in the 'Main' folder.
5. Replace "Your API Key" with your own OpenAI secret API Key.
6. Navigate to the Main folder:
```terminal
cd Main
```
7. Run the main script:
```terminal
python main.py
```
or
```terminal
python3 main.py
```
Ensure that you have followed the above steps correctly to successfully install and run Eve.

## Contributing
I welcome contributions from the community! If you'd like to contribute to Eve, here are a few ways you can help:
* **Report bugs**: If you find a bug in the code, please submit an issue on my GitHub repository.
* **Suggest features**: If you have an idea for a new feature, please let us know by creating a GitHub issue.
* **Improve the documentation**: If you notice any errors or inconsistencies in the documentation, feel free to submit a pull request with your proposed changes.
* **Improve the Chatbot**: Developers who wish to contribute can access the model training code in the folder "[Use Only for Training the Chatbot]". They can edit the "intent.json" file as per their requirements and retrain the model. They need to update the code inside the file "[assistant_gpt.py]" in the "**Main**" folder accordingly. Any contributions to improve the program are highly appreciated.

## License
This project is licensed under the MIT License. See the [LICENSE] file for more information.

## Author
Created by Mohammad Dudin


[Use Only for Training the Chatbot]: https://github.com/Xecutioner13/Eve-AI-Assistant/tree/main/Use%20Only%20for%20Training%20the%20Chatbot
[assistant_gpt.py]: https://github.com/Xecutioner13/Eve-AI-Assistant/blob/main/Main/assistant_gpt.py
[LICENSE]: https://github.com/Xecutioner13/Eve-AI-Assistant/blob/main/LICENSE
