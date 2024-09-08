# Creating QASM scripts for Trotterized TFIM.
import numpy as np
from .builder import Builder

def first_order(N: int, T: float, dt: float):
    num_steps = int(np.ceil(T / dt))
    qasm = Builder(N)
    for _ in range(num_steps):
        # x rotations
        for j in range(N):
            qasm.rx(j, 2*dt)    

        # zz rotations
        for j in range(0, N-1, 2):
            qasm.rzz(j, j+1, 2*dt)
        for j in range(1, N-1, 2):
            qasm.rzz(j, j+1, 2*dt)

    # Measurement 
    qasm.measure_all()
    return qasm 

def second_order(N: int, T: float, dt: float):
    num_steps = int(np.ceil(T / dt))
    qasm = Builder(N)
    for step in range(num_steps):
        # x rotation
        for j in range(N):
            # intermediate has step dt, first has step dt / 2
            qasm.rx(j, dt if step == 1 else 2*dt)
        
        # zz rotations
        for j in range(0, N-1, 2):
            qasm.rzz(j, j+1, 2*dt)
        for j in range(1, N-1, 2):
            qasm.rzz(j, j+1, 2*dt)
    
    # final x rotation 
    for j in range(N):
        qasm.rx(j, dt)
    
    # Measurement 
    qasm.measure_all()
    return qasm 