import numpy as np
import pygame, pygame.sndarray
import pickle
import time
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer


def playnotes(freqs,volumes): # list of frequencies and volumes
	pygame.mixer.init()
	sample_wave=sum([np.resize(volume*16384*np.sin(np.arange(int(44100/float(hz)))*np.pi*2/(44100/float(hz))),(44100,)).astype(np.int16) for hz,volume in zip(freqs,volumes)])
	stereo = np.vstack((sample_wave, sample_wave)).T.copy(order='C')
	sound = pygame.sndarray.make_sound(stereo)
	sound.play(-1)
	pygame.time.delay(600)
	sound.stop()
	pygame.time.delay(200)

def quantumnotes(qc,shots):
	midi_conversion_tables = pickle.load(open('midi_conversion_tables.p','rb'))
	midi_to_note_bin = midi_conversion_tables['midi_to_note_bin']
	midi_to_frequency_bin = midi_conversion_tables['midi_to_frequency_bin']

	backend = Aer.get_backend('qasm_simulator')
	for i in range(shots):
		sim = execute(qc,backend=backend,shots=1)
		result = sim.result()
		final = result.get_counts(qc)
		[print(midi_to_note_bin[k]) for k in final.keys()]
		playnotes([float(midi_to_frequency_bin[k]) for k in final.keys()],[1,0])

def quantumchords(qc,shots):
	midi_conversion_tables = pickle.load(open('midi_conversion_tables.p','rb'))
	midi_to_note_bin = midi_conversion_tables['midi_to_note_bin']
	midi_to_frequency_bin = midi_conversion_tables['midi_to_frequency_bin']

	backend = Aer.get_backend('qasm_simulator')
	sim = execute(qc,backend=backend,shots=shots)
	result = sim.result()
	final = result.get_counts(qc)

	freqs = []
	volumes = []
	for k,v in final.items():
		try:
			freqs+=[float(midi_to_frequency_bin[k])]
			volumes+=[int(v)/shots]
			print('%f percent' % (int(v)/shots*100),midi_to_note_bin[k])
		except:
			print('%f percent' % (int(v)/shots*100),k)
            
	playnotes(freqs,volumes)

qr = QuantumRegister(7)
cr = ClassicalRegister(7)
qc =QuantumCircuit(qr,cr)

qc.x(qr[0])
qc.x(qr[6])
qc.h(qr[2])

for i in range(7):
	qc.measure(qr[i],cr[i])

quantumnotes(qc,4)
quantumchords(qc,4)