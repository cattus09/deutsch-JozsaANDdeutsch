import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)

#ENTRADA DEL CIRCUITO
#01
#circuit.x(1)

#10
#circuit.x(0)

#11
#circuit.x(0)
#circuit.x(1)

circuit.barrier(0,1)

##(0,1) -> (0,1)
circuit.cx(0,1)

circuit.barrier(0,1)

#MEDIDORES
circuit.measure([1,0], [0,1])


compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)

print("\nTotal count for 00 and 11 are:",counts)
print(circuit)
plot_histogram(counts)
plt.show()