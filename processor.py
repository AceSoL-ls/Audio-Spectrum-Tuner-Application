import pyaudio
import numpy

class AudioProcessor:
    def __init__(self):

        self.CHUNK = 3200
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100


        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )

    def read_chunk(self):
        raw = self.stream.read(self.CHUNK)
        arr = numpy.frombuffer(raw, dtype=numpy.int16)
        return arr