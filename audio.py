import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import sample
from pygame.mixer import Channel

# Variable Settings based on our hardware or purposes
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 160000

pa = pyaudio.PyAudio()

# Here is how microphone is streaming
stream = pa.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print('Start Recording')

seconds = 8
frames = []
second_tracking = 0
second_count = 0

# Basic loop for recording
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
    second_tracking += 1
    if second_tracking == RATE/FRAMES_PER_BUFFER:
        second_count += 1
        second_tracking = 0
        print(f'Time Left: {seconds - second_count}')

stream.stop_stream()
stream.close()
pa.terminate()

# Here is how the recording is being stored as a wav file
obj = wave.open('Recording.wav', 'wb')
obj.setnchannels(CHANNELS)
obj.setsampwidth(pa.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b''.join(frames))
obj.close()

#file = wave.open('Recording.wav', 'rb')

