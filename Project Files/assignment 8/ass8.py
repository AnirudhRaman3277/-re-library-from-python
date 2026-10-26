import re

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Parser:
    def __init__(self, expression):
        # Clean whitespaces and tokenize the expression
        self.tokens = re.findall(r'[a-zA-Z0-9]+|[\+\-\*/\(\)]', expression.replace(" ", ""))
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        token = self.peek()
        if expected and token != expected:
            raise ValueError(f"Error: Expected '{expected}', found '{token}'")
        if token:
            self.pos += 1
        return token

    def parse(self):
        try:
            if not self.tokens:
                raise ValueError("Error: Empty expression.")
            
            tree = self.parse_expression()
            
            # If there are leftover tokens, the expression is invalid
            if self.pos < len(self.tokens):
                raise ValueError(f"Error: Unexpected token '{self.peek()}' at position {self.pos}")
            return tree
        except ValueError as e:
            print(e)
            return None

    # Handles + and -
    def parse_expression(self):
        node = self.parse_term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.parse_term()
            node = Node(op, left=node, right=right)
        return node

    # Handles * and /
    def parse_term(self):
        node = self.parse_factor()
        while self.peek() in ('*', '/'):
            op = self.consume()
            right = self.parse_factor()
            node = Node(op, left=node, right=right)
        return node

    # Handles numbers, variables, and parentheses
    def parse_factor(self):
        token = self.peek()
        if token == '(':
            self.consume('(')
            node = self.parse_expression()
            self.consume(')')
            return node
        elif token and (token.isalnum()):
            self.consume()
            return Node(token)
        else:
            raise ValueError(f"Error: Invalid or missing operand near '{token if token else 'EOF'}'")

# Helper function to print the tree hierarchically in text format
def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("├── " if is_left else "└── ") + str(node.value))
        new_prefix = prefix + ("│   " if is_left else "    ")
        if node.left or node.right:
            print_tree(node.left, new_prefix, True)
            print_tree(node.right, new_prefix, False)

# --- Main Program Execution ---
if __name__ == "__main__":
    expr = input("Enter an arithmetic expression (using +, -, *, / only): ")
    
    parser = Parser(expr)
    syntax_tree = parser.parse()
    
    if syntax_tree:
        print("\nGenerated Syntax Tree Structural Output:")
        print_tree(syntax_tree, is_left=False)