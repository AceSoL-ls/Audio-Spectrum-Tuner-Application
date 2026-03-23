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
RATE = 44100

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

# This is how our file gets rendered as graph!
file = wave.open('Recording.wav', 'rb')

sample_freq = file.getframerate()
frames = file.getnframes()
signal_wave = file.readframes(-1)

file.close()

time = frames / sample_freq

audio_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, time, num=frames)

# Graph Window Settings
plt.figure(figsize=(15, 5))
plt.plot(times, audio_array)
plt.ylabel('Signal Wave')
plt.xlabel('Time (s)')
plt.xlim(0, time)
plt.title('My Audio Recording! ')
plt.show()

