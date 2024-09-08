from src.qasmbuilder import builder, tfim

qasm = builder.Builder(6)

qasm.x(0)
qasm.y(1)
qasm.z(2)
qasm.rx(3, 0.565)
qasm.ry(4, 0.123)
qasm.rz(5, 0.05)
qasm.cnot(0, 1)
qasm.cnot(2, 3)
qasm.rzz(1, 3)


#print(qasm.qasm)

trotter1 = tfim.second_order(6, 1.0, 0.1)
print(trotter1.qasm)
trotter1.save("trotter.qasm")