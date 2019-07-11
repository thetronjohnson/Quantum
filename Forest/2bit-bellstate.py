from pyquil import Program, get_qc
from pyquil.gates import *

p = Program()
ro = p.declare('ro', 'BIT', 2)
p += H(0)
p += CNOT(0, 1)
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])

qc = get_qc('2q-qvm')
exe = qc.compile(p)
result = qc.run(exe)
print(result)