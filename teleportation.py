from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import math  # from main branch (HEAD)
import numpy as np  # from dev branch


# How to use this protocole:
#   1. Prepare a quantum circuit with 3 qubits. Let's name this circuit "init_qc"
#   2. Place qubit 0 in "init_qc" in a quantum state of your choice
#   3. Combine your circuit with the `teleportation` circuit defined below
#   4. After execution, qubit 3 is now in the state of your choice!
qr = QuantumRegister(3, name="q")
crz, crx = ClassicalRegister(1, name="crz"), ClassicalRegister(1, name="crx")
crb = ClassicalRegister(1, name="crb")
teleportation = QuantumCircuit(qr, crz, crx, crb)

teleportation.h(1)
teleportation.cx(1, 2)
teleportation.cx(0, 1)
teleportation.h(0)

teleportation.measure(0, 0)
teleportation.measure(1, 1)

with teleportation.if_test((crx, 1)):
        teleportation.x(2)
with teleportation.if_test((crz, 1)):
    teleportation.z(2)
