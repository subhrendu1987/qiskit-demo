from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import GroverOperator

# Define the oracle
def oracle(circuit, qubits):
    """
    Oracle marks the state |11> as the solution.
    This is achieved by applying a controlled-Z gate.
    """
    circuit.cz(qubits[0], qubits[1])

# Create Grover's Algorithm Quantum Circuit
def grovers_algorithm():
    # Define a 2-qubit quantum circuit
    n_qubits = 2
    qc = QuantumCircuit(n_qubits)

    # Step 1: Apply Hadamard gates to all qubits
    qc.h(range(n_qubits))

    # Step 2: Apply the oracle
    oracle(qc, range(n_qubits))

    # Step 3: Apply Grover diffusion operator
    qc.h(range(n_qubits))  # Hadamard on all qubits
    qc.x(range(n_qubits))  # X gates
    qc.cz(0, 1)            # Controlled-Z gate
    qc.x(range(n_qubits))  # X gates
    qc.h(range(n_qubits))  # Hadamard on all qubits

    # Measure the qubits
    qc.measure_all()
    return qc

# Execute the circuit
def run_grovers():
    qc = grovers_algorithm()
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()
    return qc, counts

# Run Grover's algorithm and visualize results
if __name__ == "__main__":
    qc, counts = run_grovers()
    print("Quantum Circuit:")
    print(qc)
    print("\nResults:")
    print(counts)
    plot_histogram(counts).show()
