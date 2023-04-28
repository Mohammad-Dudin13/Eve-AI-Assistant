from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

class TextToSpeech:
    """
    This class is used to convert text to speech using the Google Text-to-Speech API and play the resulting audio.
    """
    def play_audio(self, answer):
        """
        Converts the provided answer text to speech using Google's Text-to-Speech API and plays the resulting audio.

        Args:
            answer (str): The answer text to be converted to speech.

        Returns:
            None
        """
        if not answer:
            # If the answer is empty, return without playing anything
            return
        # Create an in-memory file object to hold the audio data
        fp = BytesIO()
        # Use the Google Text-to-Speech API to convert the answer to speech and write the resulting audio to the file object
        tts = gTTS(text=answer, lang='en', tld='co.uk', slow=False)
        tts.write_to_fp(fp)
        # Reset the file object's position to the beginning
        fp.seek(0)
        # Load the audio data from the file object using PyDub
        audio = AudioSegment.from_file(fp, format="mp3")
        # Play the audio using PyDub's playback function
        play(audio)