from src.qasmbuilder import builder

qasm = builder.Builder(6)

qasm.x(qasm, 0)
qasm.y(qasm, 1)
qasm.z(qasm, 2)
qasm.rx(qasm, 3, 0.565)
qasm.ry(qasm, 4, 0.123)
qasm.rz(qasm, 5, 0.05)
qasm.cnot(qasm, 0, 1)
qasm.cnot(qasm, 2, 3)


print(qasm.qasm)