from pyquil.quil import Program
from pyquil.gates import *
from pyquil import get_qc

p = Program()
ro = p.declare('ro','BIT',1)
p += X(0)
p += MEASURE(0,ro[0])

qc = get_qc('1q-qvm')
exe = qc.compile(p)
result = qc.run(exe)
print(result)