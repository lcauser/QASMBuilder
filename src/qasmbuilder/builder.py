# The base class for building QASM scripts
import numpy as np

class Builder:
    """
    Base class for building QASM scripts.
    """

    def __init__(self, num_qubits: int, version=3.1):
        self.num_qubits = num_qubits
        self.num_cbits = num_qubits # Maybe add choice later
        self.version = version

        # Initiliase
        self.qasm = f"OPENQASM {self.version}; \n"
        self.qasm += f"include \"stdgates.inc\";\n\n"
        self.qasm += f"qubit[{self.num_qubits}] q; \n"
        self.qasm += f"bit[{self.num_cbits}] c; \n\n"


    # Checking that the qubit lives within the register 
    def _check_qubit(self, qubit: int):
        if qubit >= 0 and qubit < self.num_qubits:
            return True
        raise Exception("The specified qubits are not in the register.")

    ### Single body gates
    # Redundancy: each gate addition is basically the same, so lets streamline it.
    def _one_qubit_gate(self, qasm:str, qubit: int, gate: str):
        self._check_qubit(qubit)
        self.qasm += f"{gate} q[{qubit}]; \n"

    def x(self, qasm: str, qubit: int):
        """
        Add an X gate at a qubit.
        """
        self._one_qubit_gate(qasm, qubit, "x")
    
    def y(self, qasm: str, qubit: int):
        """
        Add a Y gate at a qubit.
        """
        self._one_qubit_gate(qasm, qubit, "y")
    
    def z(self, qasm: str, qubit: int):
        """
        Add a Z gate at a qubit.
        """
        self._one_qubit_gate(qasm, qubit, "z")
    
    def hadamard(self, qasm: str, qubit: int):
        """
        Add a Hadamard gate at a qubit.
        """
        self._one_qubit_gate(qasm, qubit, "h")

    def rx(self, qasm: str, qubit: int, theta: float = np.pi):
        """
        A an X-rotation gate at a qubit. The angle of the rotation is theta.
        """
        self._one_qubit_gate(qasm, qubit, f"rx({theta})")
    
    def ry(self, qasm: str, qubit: int, theta: float = np.pi):
        """
        A a Y-rotation gate at a qubit. The angle of the rotation is theta.
        """
        self._one_qubit_gate(qasm, qubit, f"ry({theta})")
    
    def rz(self, qasm: str, qubit: int, theta: float = np.pi):
        """
        A a Z-rotation gate at a qubit. The angle of the rotation is theta.
        """
        self._one_qubit_gate(qasm, qubit, f"rz({theta})")
    

    ### Two qubit gates
    # Redundancy: each gate addition is basically the same, so lets streamline it.
    def _two_qubit_gate(self, qasm:str, q1: int, q2: int, gate: str):
        self._check_qubit(q1) and self._check_qubit(q2)
        self.qasm += f"{gate} q[{q1}] q[{q2}]; \n"
    
    def cnot(self, qasm: str, control: int, target: int):
        """
        Add a CNOT gate at a control qubit and target qubit.
        """
        self._two_qubit_gate(qasm, control, target, "cx")
    

