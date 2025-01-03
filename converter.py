# Fabio Tiberio SM3201378
from assembler import Assembler
from lmc import LMC
from lmc_exceptions import EmptyInputQueueException, HaltException

# Classe "ponte" tra LMC e Assembler
# Rende la visualizzazione di risultati nel main.py un po'più ordinata
# Permette una maggiore "separazione" delle responsabilità dei vari oggetti
class Converter:
    def __init__(self, filename):
        self.filename = filename
        self.assembler = Assembler(filename)
        self.lmc = LMC()


    def load_memory(self):
        return self.assembler.load_memory()


    def resolve_labels(self, instructions):
        resolved_instructions = self.assembler.identify_labels(instructions)
        self.assembler.replace_labels(resolved_instructions)
        return resolved_instructions


    def get_machine_codes(self, resolved_instructions):
        machine_codes = []
        for instruction in resolved_instructions:
            machine_codes.append(self.parse_assembly(instruction))
        return machine_codes


    # Funzioni nel caso in cui ci sia l'input dell'utente
    def clean_input(self, instruction):
        self.assembler.instruction_normalization([instruction])


    def parse_assembly(self, instruction):
        machine_code = None
        if len(instruction) == 2:
            machine_code = self.assembler.parse_assembly_action(instruction)
        if len(instruction) == 1:
            machine_code = self.assembler.parse_assembly_inout(instruction)
        # qui dovrei gestire l'assenza di dato
        return machine_code


    def feed_lmc(self, machine_codes, input = []):
        self.lmc.initialize_memory(machine_codes, input)


    def run_lmc(self):
        try:
            self.lmc.run()
        except EmptyInputQueueException as e:
            print(e)
        except HaltException as e:
            print(e)
        except Exception as e:
            print(e)


    def can_continue(self):
        return not self.lmc.halted


    def summary(self):
        return Summary(self.lmc.program_counter, self.lmc.accumulator, self.lmc.cells, self.lmc.output_queue, self.lmc.input_queue)


    def run_lmc_step(self):
        self.lmc.run_step()


    def get_results(self):
        return self.lmc.output_queue.items


class Summary:
    def __init__(self, program_counter, accumulator, memory, output_queue, input_queue):
        self.program_counter = program_counter
        self.accumulator = accumulator
        self.memory = memory
        self.input_queue = input_queue
        self.output_queue = output_queue


    def __str__(self):
        memory_state = "\n".join([f"{i:02d}: {cell.content}" for i, cell in enumerate(self.memory)])

        return (
            f"--- LMC Summary ---\n"
            f"Program Counter: {self.program_counter}\n"
            f"Accumulatore: {self.accumulator}\n"
            f"Coda di Input:\n{self.input_queue.items}\n"
            f"Coda di Output:\n{self.output_queue.items}\n"
            f"Memoria:\n{memory_state}\n"
            f"-------------------"
        )










