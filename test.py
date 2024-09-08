from src.qasmbuilder import builder

qasm = builder.Builder(6)

qasm.x(0)
qasm.y(1)
qasm.z(2)
qasm.rx(3, 0.565)
qasm.ry(4, 0.123)
qasm.rz(5, 0.05)
qasm.cnot(0, 1)
qasm.cnot(2, 3)


print(qasm.qasm)