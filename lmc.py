# Fabio Tiberio SM3201378
from lmc_exceptions import *
from queue import Queue
from cell import *

class LMC:

    def __init__(self):
        self.cells = [Cell() for _ in range(100)]
        self.accumulator = 0
        self.program_counter = 0
        self.input_queue = Queue()
        self.output_queue = Queue()
        self.flag = False  # False: within 0...999; True: out of range
        self.halted = False

        self.instructions = {
            1: self.sum,
            2: self.sub,
            3: self.store,
            5: self.load,
            6: self.branch,
            7: self.branch_if_zero,
            8: self.branch_if_positive,
            9: self.io
        }

    def fetch(self):
        """
        Recupera la cella corrente dalla memoria e incrementa il program counter.
        """
        if not (0 <= self.program_counter < len(self.cells)):
            raise IndexError("Program counter fuori dai limiti.")
        cell = self.cells[self.program_counter]
        self.program_counter += 1
        return cell

    def decode_and_execute(self, cell: Instruction):
        """
        Decodifica ed esegue un'istruzione.
        """
        if cell.opcode in self.instructions:
            self.instructions[cell.opcode](cell.address)
        else:
            raise ValueError(f"Opcode non valido: {cell.opcode}")

    def sum(self, address: int):
        """
        Somma il contenuto della cella all'accumulatore.
        """
        value = self._get_cell_value(address)
        self.accumulator = (self.accumulator + value) % 1000
        self.flag = self.accumulator < 0 or self.accumulator > 999

    def sub(self, address: int):
        """
        Sottrae il contenuto della cella all'accumulatore.
        """
        value = self._get_cell_value(address)
        self.accumulator = (self.accumulator - value) % 1000
        self.flag = self.accumulator < 0 or self.accumulator > 999

    def store(self, address: int):
        """
        Memorizza il valore dell'accumulatore in una cella.
        """
        self._validate_address(address)
        self.cells[address].content = self.accumulator

    def load(self, address: int):

        self.accumulator = self._get_cell_value(address)

    def branch(self, address: int):
        self.program_counter = address

    def branch_if_zero(self, address: int):
        if self.accumulator == 0 and not self.flag:
            self.program_counter = address

    def branch_if_positive(self, address: int):
        if not self.flag:
            self.program_counter = address

    def io(self, address: int):
        if address == 1:
            if self.input_queue.isEmpty():
                raise EmptyInputQueueException("Coda di input vuota.")
            self.accumulator = self.input_queue.dequeue()
        elif address == 2:
            self.output_queue.enqueue(self.accumulator)

    def initialize_memory(self, machine_codes, input=[]):
        for value in input:
            self.input_queue.enqueue(value)
        for i, code in enumerate(machine_codes):
            if code[0] is not None:
                self.cells[i] = Instruction(code[0], code[1])
            else:
                self.cells[i] = Content(code[1])

    def _get_cell_value(self, address: int) -> int:
        self._validate_address(address)
        cell = self.cells[address]
        if isinstance(cell, Content):
            return cell.content
        raise HaltException("Tentativo di interpretare un dato come istruzione.")

    def _validate_address(self, address: int):
        if not (0 <= address < len(self.cells)):
            raise IndexError(f"Indirizzo {address} fuori dai limiti.")

    def run(self):
        while not self.halted:
            try:
                self.perform_step()
            except HaltException as e:
                print(f"Errore: {e}")
                self.halted = True
            except Exception as e:
                print(f"Errore: {e}")
                self.halted = True

    def run_step(self):
        if not self.halted:
            try:
                self.perform_step()
            except HaltException as e:
                print(f"Errore: {e}")
                self.halted = True
            except Exception as e:
                print(f"Errore: {e}")
                self.halted = True

    def perform_step(self):
        cell = self.fetch()
        if isinstance(cell, Content):
            raise HaltException("Dato interpretato come istruzione")
        elif isinstance(cell, Instruction):
            if cell.opcode == 0:
                self.halted = True
            else:
                self.decode_and_execute(cell)
