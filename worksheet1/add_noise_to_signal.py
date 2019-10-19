import soundfile as sf
import numpy as np

data, samplerate = sf.read('Market Square.wav')
noise = np.random.normal(scale=0.5, size=data.shape)

mix = noise + data

sf.write('noisey_song.flac', mix, samplerate)
