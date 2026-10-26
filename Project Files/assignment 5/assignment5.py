import re


class SymbolTable:
    def __init__(self, symbol, symbol_type, line_no, address, storage_bytes):
        self.symbol = symbol
        self.symbol_type = symbol_type
        self.line_no = line_no
        self.address = address
        self.bytes = storage_bytes


if __name__ == '__main__':

    filename = "assignment5_input.c"

    with open(filename, "r") as file:
        content = file.read()

    print("The C code is as follows:\n")
    print("ORIGINAL CODE")
    print("------------------------------------------------------------\n")
    print(content, "\n")
    print("------------------------------------------------------------\n")

    data_type_size = {
        "char": 1,
        "int": 4,
        "float": 4,
        "double": 8
    }

    content = re.sub(r'/\*[\s\S]*?\*/', '', content)
    content = re.sub(r'//.*', '', content)

    address = 0x1000
    table = []

    declaration_pattern = re.compile(
        r'\b(int|float|char|double)\s+'
        r'([a-zA-Z_][a-zA-Z0-9_]*)(?:\s*\[\s*(\d+)\s*\])?'
    )

    print(declaration_pattern)

    for line_no, line in enumerate(content.splitlines(), start=1):

        matches = declaration_pattern.finditer(line)

        for match in matches:

            data_type = match.group(1)
            symbol = match.group(2)
            array_size = match.group(3)

            if any(x.symbol == symbol for x in table):
                continue

            if array_size is None:
                storage_bytes = data_type_size[data_type]
                symbol_type = data_type

            else:
                storage_bytes = data_type_size[data_type] * int(array_size)
                symbol_type = data_type + "[" + array_size + "]"

            table.append(
                SymbolTable(
                    symbol,
                    symbol_type,
                    line_no,
                    address,
                    storage_bytes
                )
            )

            address += storage_bytes

    print("\nSYMBOL TABLE")
    print("------------------------------------------------------------\n")
    print(
        f"{'Symbol':<15}"
        f"{'Data Type':<15}"
        f"{'Line No.':<12}"
        f"{'Address':<12}"
        f"{'Bytes':<10}"
    )

    print(" ")

    for item in table:
        print(
            f"{item.symbol:<15}"
            f"{item.symbol_type:<15}"
            f"{item.line_no:<12}"
            f"{item.address:04X}{'':<8}"
            f"{item.bytes:<10}"
        )

    print(" ")
