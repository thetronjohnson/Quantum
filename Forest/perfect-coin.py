from pyquil.quil import Program
from pyquil.gates import *
from pyquil import get_qc

outcomes = {
	
	'heads':1,
	'tails':0
}


p = Program()
ro = p.declare('ro','BIT',1)
p += H(0)
p += MEASURE(0,ro[0])

qc = get_qc('1q-qvm')
exe = qc.compile(p)


print("Guess the outcome!\n")
coin_toss = p.measure_all()
guess = input("heads or tails?")
result = qc.run(exe)
try:
	if(result==outcomes[guess]):
		print("Your guessed right!!\n")
	else:
		print("Oops! Wrong guess")
except:
	pass