import cirq

#length of grid
length = 3

#qubits on grid
qubits = [cirq.GridQubit(i,j) for i in range(length) for j in range(length)]

circuit = cirq.Circuit()
circuit.append([cirq.H(q) for q in qubits if(q.row + q.col) % 2 == 0],strategy=cirq.InsertStrategy.EARLIEST)
circuit.append([cirq.X(q) for q in qubits if (q.row + q.col) % 2 ==1],strategy=cirq.InsertStrategy.NEW_THEN_INLINE)

for i,m in enumerate(circuit):
    print(f"Moment {i}:{m}")