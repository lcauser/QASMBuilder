from src.qasmbuilder import builder

builder = builder.Builder(6)
qasm = builder.initialise()

qasm = builder.x(qasm, 0)
qasm = builder.y(qasm, 1)
qasm = builder.z(qasm, 2)
qasm = builder.rx(qasm, 3, 0.565)
qasm = builder.ry(qasm, 4, 0.123)
qasm = builder.rz(qasm, 5, 0.05)
qasm = builder.cnot(qasm, 0, 1)
qasm = builder.cnot(qasm, 2, 3)


print(qasm)