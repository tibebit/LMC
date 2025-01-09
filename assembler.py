# Fabio Tiberio SM3201378
from lmc import LMC
from lmc_exceptions import *

class Assembler:

    instruction_map = {
        "ADD": 1,
        "SUB": 2,
        "STA": 3,
        "LDA": 5,
        "BRA": 6,
        "BRZ": 7,
        "BRP": 8,
        "INP": 901,
        "OUT": 902,
        "HLT": 0,
        "DAT": None
    }

    def __init__(self, filename):
        self.lmc = LMC()
        self.filename = filename
        self.labels = {}
        self.instructions_given = 0

    def load_memory(self):
        instr = []
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.split('//')[0].strip()
                    # se la riga non è vuota, aggiungila all'array
                    if line:
                        instr.append(self.instruction_normalization(line))
                        self.instructions_given += 1
        except FileNotFoundError:
            print(f"Errore: Il file '{self.filename}' non è stato trovato.")
        except Exception as e:
            print(f"Errore durante la lettura del file: {e}")\

        return instr

    def instruction_normalization(self, instruction):
        return ' '.join(instruction.upper().split())


    def parse_assembly_action(self, instruction):
        #word = instruction[0]  # nome instruzione
        #code = instruction[1]  # valore eventuale
        machine_code = 0

        try:
            #machine_code = self.parse_assembly_word([word])
            #machine_code += int(code)
            opcode = self.parse_assembly_word([instruction[0]])
            operand = int(instruction[1])

        except InstructionNotFoundException:
            pass
        except ValueError:
            # Code era una stringa. Sta nei labels?
            try:
                machine_code += self.search_label(instruction[1])
            except LabelNotFoundException:
                pass
        except Exception as e:
            print("Passato di qua")

        self.instructions_given += 1
        #return machine_code
        return [opcode, operand]

    def parse_assembly_inout(self, instruction):
        value = 0
        if self.word_to_code(instruction[0]) is not None:
            value += self.word_to_code(instruction[0])
        else:
            return [None, value]
        self.instructions_given += 1

        return [value // 100, value % 100]

    def parse_assembly_word(self, instruction):
        value = 0
        if self.word_to_code(instruction[0]) is not None:
            value += self.word_to_code(instruction[0])
        else:
            value = None
        self.instructions_given += 1
        return value

    # Devo mettere in conto il fatto che DAT non abbia il None
    def word_to_code(self, word):
        if word in self.instruction_map:
            return self.instruction_map[word]
        else:
            raise InstructionNotFoundException

    # Identifica le etichette, ne salva l'indirizzo e le rimuove.
    def identify_labels(self, instructions):
        wiped_instructions = []
        for i, instruction in enumerate(instructions):
            parts = instruction.split()
            if len(parts) == 3:
                self.labels[parts[0]] = i
                del parts[0]

            # In caso ci siano solo due istruzioni, la prima potrebbe essere una etichetta
            elif len(parts) == 2:
                if parts[0] not in self.instruction_map.keys():
                    self.labels[parts[0]] = i
                    del parts[0]

            wiped_instructions.append(parts)

        return wiped_instructions

    # Sostituisce l'etichetta indicata dall'istruzione con l'indirizzo di memoria opportuno
    def replace_labels(self, instructions):
        for instruction in instructions:
            if instruction[-1] in self.labels:
                instruction[-1] = self.labels[instruction[-1]]

    # Cerca tra i label esistenti
    def search_label(self, label):
            if label in self.labels:
                return self.labels[label]
            else:
                raise LabelNotFoundException











