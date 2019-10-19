import soundfile as sf
import numpy as np


def play_note(n, duration):
    a = 440
    freq = a * 2**((n-69)/12)

    srate = 44100
    t = np.linspace(0, duration, srate * duration)
    sinewav = np.sin(2 * np.pi * freq * t)
    sf.write('sine.wav', sinewav, srate)


play_note(69, .5)
sleep(.1)
play_note(72, .5)
sleep(.1)
play_note(75, .5)