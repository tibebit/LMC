class Cell:

    def __init__(self, content=None):
        if content is not None and not isinstance(content, int):
            raise ValueError("Il contenuto della cella non è valido")
        self._content = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, int):
            raise ValueError("Il contenuto della cella deve essere un numero intero.")
        self._content = value

    def __repr__(self):
        return f"{self._content}"


class Instruction(Cell):
    """
    Rappresenta una cella che contiene un'istruzione.
    """
    def __init__(self, opcode, address):
        if not isinstance(opcode, int) or not (0 <= opcode <= 9):
            raise ValueError("Opcode deve essere un intero tra 0 e 9.")
        if not isinstance(address, int) or not (0 <= address <= 99):
            raise ValueError("Address deve essere un intero tra 0 e 99.")
        super().__init__((opcode * 100) + address)
        self._opcode = opcode
        self._address = address

    @property
    def opcode(self):
        """Restituisce l'opcode dell'istruzione."""
        return self._opcode

    @property
    def address(self):
        """Restituisce l'indirizzo dell'istruzione."""
        return self._address

    def __repr__(self):
        return f"{self.content})"


class Content(Cell):
    """
    Rappresenta una cella che contiene un dato.
    """
    def __init__(self, content):
        if not isinstance(content, int):
            raise ValueError("Il contenuto deve essere un numero intero.")
        super().__init__(content)

    def __repr__(self):
        return f"{self.content}"
