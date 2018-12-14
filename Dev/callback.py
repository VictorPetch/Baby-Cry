import pyaudio
from pyaudio import PyAudio, paFloat32
import time
pa = pyaudio.PyAudio()
def callback(in_data, frame_count, time_info, status):
    print("aaaaaaaaaaaaaaaaa")
    return (in_data, pyaudio.paContinue)
stream = pa.open(format = paFloat32,
                     channels = 1,
                     rate = 44100,
                     output = True,
                     frames_per_buffer = 1024,
                     stream_callback = callback)

while stream.is_active():
    print("bbbbbbbbb")
    time.sleep(0.1)
       
print("ccccccc")
stream.close()
pa.terminate()
