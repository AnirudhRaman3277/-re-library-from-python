import re

keywords = {
    "int", "float", "double", "char", "bool", "void",
    "if", "else", "for", "while", "do", "return",
    "break", "continue", "switch", "case", "default",
    "struct", "long", "short", "signed", "unsigned",
    "const", "static"
}

operators_set = {
    "+", "-", "*", "/", "%", "=",
    "==", "!=", "<", ">", "<=", ">=",
    "++", "--",
    "+=", "-=", "*=", "/=", "%=",
    "&=", "|=", "^=",
    "&&", "||", "&", "|", "^",
    "->", "~", "?", ":",
    "(", ")", "{", "}", "[", "]", ";", ","
}

token_patterns_ordered = [
    ("COMMENT", r"//[^\n]*|/\*[\s\S]*?\*/"),
    ("WHITESPACE", r"\s+"),
    ("NUMBER", r"\b\d+(?:\.\d+)?\b"),
    ("OPERATOR", r"\+=|-=|\*=|/=|%=|&=|\|=|\^=|==|!=|<=|>=|\+\+|--|&&|\|\||->|[+\-*/%=<>!&|^~?:()\[\]{},;]"),
    ("IDENTIFIER", r"[A-Za-z_][A-Za-z0-9_]*"),
]


def tokenAnalyzer(content):
    if not content:
        print("The content is empty")
        return

    counts = {
        "Keywords": 0,
        "Identifiers": 0,
        "Operators": 0,
        "Numbers": 0,
        "Total Tokens": 0
    }

    pos = 0

    while pos < len(content):
        match = None

        for token_type, pattern in token_patterns_ordered:
            regex = re.compile(pattern)
            match = regex.match(content, pos)

            if match:
                token = match.group(0)

                if token_type == "COMMENT":
                    pass

                elif token_type == "WHITESPACE":
                    pass

                elif token_type == "NUMBER":
                    counts["Numbers"] += 1
                    counts["Total Tokens"] += 1
                    print(f"NUMBER      : {token}")

                elif token_type == "IDENTIFIER":
                    if token in keywords:
                        counts["Keywords"] += 1
                        counts["Total Tokens"] += 1
                        print(f"KEYWORD     : {token}")
                    else:
                        counts["Identifiers"] += 1
                        counts["Total Tokens"] += 1
                        print(f"IDENTIFIER  : {token}")

                elif token_type == "OPERATOR":
                    if token in operators_set:
                        counts["Operators"] += 1
                        counts["Total Tokens"] += 1
                        print(f"OPERATOR    : {token}")

                pos = match.end()
                break

        if not match:
            print(
                f"Warning: Unknown token '{content[pos]}' "
                f"at position {pos}"
            )
            pos += 1

    print("\nLexical Analysis Results:")
    print(f"Keywords: {counts['Keywords']}")
    print(f"Identifiers: {counts['Identifiers']}")
    print(f"Operators: {counts['Operators']}")
    print(f"Numbers: {counts['Numbers']}")
    print(f"Total Tokens: {counts['Total Tokens']}")


if __name__ == '__main__':
    filename = "assignment4_input.c"

    try:
        with open(filename, "r") as file:
            content = file.read()

        print("The C code is as follows:\n")
        print("ORIGINAL CODE")
        print("------------------------------------------------------------\n")
        print(content)
        print("\n------------------------------------------------------------\n")

        tokenAnalyzer(content)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except PermissionError:
        print(f"Error: Permission denied while opening '{filename}'.")

    except Exception as e:
        print(f"Error: {e}")