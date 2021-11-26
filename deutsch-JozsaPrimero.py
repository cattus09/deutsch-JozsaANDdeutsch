import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)

#00 -> 0  
#01 -> 0 
#10 -> 1 
#11 -> 1 

#ENTRADA DEL CIRCUITO
#001
#circuit.x(2)

#010
#circuit.x(1)

#011
#circuit.x(2)
#circuit.x(1)

#100
#circuit.x(0)

#101
#circuit.x(0)
#circuit.x(2)

#110
#circuit.x(1)
#circuit.x(0)

#111
#circuit.x(2)
#circuit.x(1)
#circuit.x(0)

circuit.barrier(0,1,2)

circuit.cx(0,2)

circuit.barrier(0,1,2)

#MEDIDORES
circuit.measure([0,1,2], [2,1,0])


compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()