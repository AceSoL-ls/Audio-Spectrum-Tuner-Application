import pyaudio

from audio import pa

class AudioProcessor:
    def __init__(self):

        FRAMES_PER_BUFFER = 3200
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100


        self.pa = pyaudio.PyAudio()
        self.stream = pa.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=FRAMES_PER_BUFFER
        )

    def read_chuck(self):
        return self.stream.read(self.CHUNK)