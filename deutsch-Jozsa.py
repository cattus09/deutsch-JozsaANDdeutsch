import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 2)

#ENTRADA DEL CIRCUITO
circuit.x(2)

circuit.barrier(0,1,2)

#CIRCUITO DE DEUTSCH
circuit.h(0)
circuit.h(1)
circuit.h(2)

circuit.barrier(0,1,2)
#Uf

##[(0,0),(0,1)] -> (0)
##[(1,0),(1,1)] -> (1)
circuit.cx(0,2)

##[(0,0),(0,1),(1,0),(1,1)] -> (0)
#circuit.i(0)
#circuit.i(1)
#circuit.i(2)


circuit.barrier(0,1,2)
circuit.h(0)
circuit.h(1)


circuit.barrier(0,1,2)
#MEDIDORES
circuit.measure([0,1], [1,0])


compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()