import pyaudio

class MicrophoneMute:
    def __init__(self):
        """
        Initializes the MicrophoneMute class by creating a PyAudio instance and opening a stream for input and output.
        """
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=44100,
                                  input=True, output=True, frames_per_buffer=1024)

    def mute_microphone(self):
        """
        Stops the microphone stream, effectively muting the microphone.
        """
        self.stream.stop_stream()
        print("Microphone Stopped!")

    def unmute_microphone(self):
        """
        Starts the microphone stream, effectively unmuting the microphone.
        """
        self.stream.start_stream()
        print("Microphone Enabled!")