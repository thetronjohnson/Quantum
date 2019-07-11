from pyquil.quil import Program
from pyquil.gates import I
from pyquil.api import QVMConnection

qvm = QVMConnection()
P = Program(I(0))
print(qvm.wavefunction(P))
