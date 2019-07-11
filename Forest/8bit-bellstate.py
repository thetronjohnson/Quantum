from pyquil import Program, get_qc
from pyquil.gates import H, CNOT

qc = get_qc('8q-qvm')

# Bell State
p = Program(H(0),CNOT(0,1))

rslt = qc.run_and_measure(p,trials=10)
print(rslt)