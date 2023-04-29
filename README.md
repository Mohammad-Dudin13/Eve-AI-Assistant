# Eve-AI-Assistant
Eve is a Python-based AI assistant that utilizes a trained chatbot, TensorFlow, and OpenAI API. It offers various functionalities, including movie recommendations from IMDb, web searching via Wikipedia, and retrieving weather information for specified cities. For complex tasks like writing poems, emails, and coding, Eve leverages the power of OpenAI's API (user key required). Users communicate with Eve by providing prompts through speech, which are converted to text for processing. The generated responses are then transformed back into speech using the GTTS (Google Text-to-Speech) model, enabling a seamless and interactive user experience.
## Features
* Movie recommendations: Eve can suggest movies based on genre, year, and minimum rating using data from IMDb.
* Web searching: Utilizing Wikipedia, Eve can search the web and provide short summaries on various topics.
* Weather information: Users can request weather details for specified cities, which Eve retrieves using relevant APIs.
* Complex tasks: For advanced tasks like writing poems, emails, and coding, Eve utilizes OpenAI's API (user key required).
## Installation and Running
Follow these steps to install and run Eve (Using Terminal):
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
4. Open the main.py file located in the Main folder.
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
