class Conversion:
    def __init__(self):
        self.stack = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operand(self, char):
        return char.isalnum()

    def higher_precedence(self, op):
        return self.precedence[op] if op in self.precedence else 0

    def infix_to_postfix(self, expression):
        for char in expression:
            if self.is_operand(char):
                self.output.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  # Pop '(' from the stack
            else:
                while self.stack and self.higher_precedence(char) <= self.higher_precedence(self.stack[-1]):
                    self.output.append(self.stack.pop())
                self.stack.append(char)

        while self.stack:
            self.output.append(self.stack.pop())

        return ''.join(self.output)


# Driver code
if __name__ == '__main__':
    exp = "((A+B)*C-(D-E))^(F+G)"
    converter = Conversion()
    postfix_expression = converter.infix_to_postfix(exp)
    print("Postfix Expression:", postfix_expression)
