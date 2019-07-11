from pyquil.quil import Program
from pyquil.gates import I,H
from pyquil.api import QVMConnection

qvm = QVMConnection()
P = Program(H(0))
print(qvm.wavefunction(P))
