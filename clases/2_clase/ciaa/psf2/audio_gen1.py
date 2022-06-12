import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sc
import simpleaudio as sa

f    = 6000
fs   = 44100
sec  = 20
B    = 2000
t    = np.arange(0,sec,1/fs)

note = (2**15-1)*np.sin(2 * np.pi * B/2*(t/sec) *t)  #sweept
notes={"do":261.63,"re":293.66, "mi":329.63, "fa":349.23, "sol":392.00, "la":440.00,"si":493.88}
#chordCMajor
DOm= (2**15-1) * 0.3 * np.sin(2 * np.pi * notes["do"]  *t) +\
     (2**15-1) * 0.2 * np.sin(2 * np.pi * notes["mi"]  *t) +\
     (2**15-1) * 0.3 * np.sin(2 * np.pi * notes["sol"] *t)
#chordFMajor
FAm= (2**15-1) * 0.3 * np.sin(2 * np.pi * notes["fa"] *t) +\
     (2**15-1) * 0.2 * np.sin(2 * np.pi * notes["la"] *t) +\
     (2**15-1) * 0.3 * np.sin(2 * np.pi * notes["do"] *t)

note=FAm
#steps=10
#note=np.array([])
#for i in range(steps):
#    note=np.append(note,[(2**15-1)*np.sin(2 * np.pi * B*(i/steps) *t)])

#note = (2**15-1)*np.sin(2 * np.pi * B * t)
#note = (2**15-1)*sc.sawtooth(2 * np.pi * f * t)
#note = (2**15-1)*sc.square(2 * np.pi * f * t)

#fig=plt.figure(1)
#plt.plot(t,note)
##plt.plot(t[0:5*fs//f],note[:5*fs//f])
#plt.show()

audio = note.astype(np.int16)
for i in range(1000):
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

