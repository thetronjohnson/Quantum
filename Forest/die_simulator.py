#8 sided quantum dice

from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H
from functools import reduce

#QVM
qvm = QVMConnection()

dice = Program(H(0),H(1),H(2)) # H gate on 3 qubits to get 8 random states

roll_dice = dice.measure_all()

result = qvm.run(roll_dice)

value = reduce(lambda x,y: 2*x+y, result[0],0)+1

print("The die roll returned: ", value)