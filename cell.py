# Fabio Tiberio SM3201378

# generica cella del LMC
class Cell:

    def __init__(self, content=None):
        if content is not None and not isinstance(content, int):
            raise ValueError("Le celle accettano solo interi")
        self._content = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, int):
            raise ValueError("Le celle accettano solo interi")
        self._content = value

    def __repr__(self):
        return f"{self._content}"

# cella con istruzione
class Instruction(Cell):
    def __init__(self, opcode, address):
        if not isinstance(opcode, int) or not (0 <= opcode <= 9):
            raise ValueError("Opcode non valido")
        if not isinstance(address, int) or not (0 <= address <= 99):
            raise ValueError("Adress non valido")
        super().__init__((opcode * 100) + address)
        self._opcode = opcode
        self._address = address

    @property
    def opcode(self):
        return self._opcode

    @property
    def address(self):
        return self._address

    def __repr__(self):
        return f"{self.content})"

# data cell
class Content(Cell):
    def __init__(self, content):
        if not isinstance(content, int):
            raise ValueError("Le celle accettano solo interi")
        super().__init__(content)

    def __repr__(self):
        return f"{self.content}"
