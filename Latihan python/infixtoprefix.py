# Python code to convert infix to prefix expression


# Function to check if the character is an operator
def isOperator(c):
	return (not c.isalpha()) and (not c.isdigit())



# Function to get the priority of operators
def getPriority(c):
	if c == '-' or c == '+':
		return 1
	elif c == '*' or c == '/':
		return 2
	elif c == '^':
		return 3
	return 0



# Function to convert the infix expression to postfix
def infixToPostfix(infix):
	infix = '(' + infix + ')'
	l = len(infix)
	char_stack = []
	output = ""

	for i in range(l):
		
		# Check if the character is alphabet or digit
		if infix[i].isalpha() or infix[i].isdigit():
			output += infix[i]
			
		# If the character is '(' push it in the stack
		elif infix[i] == '(':
			char_stack.append(infix[i])
		
		# If the character is ')' pop from the stack
		elif infix[i] == ')':
			while char_stack[-1] != '(':
				output += char_stack.pop()
			char_stack.pop()
		
		# Found an operator
		else:
			if isOperator(char_stack[-1]):
				if infix[i] == '^':
					while getPriority(infix[i]) <= getPriority(char_stack[-1]):
						output += char_stack.pop()
				else:
					while getPriority(infix[i]) < getPriority(char_stack[-1]):
						output += char_stack.pop()
				char_stack.append(infix[i])

	while len(char_stack) != 0:
		output += char_stack.pop()
	return output



# Function to convert infix expression to prefix
def infixToPrefix(infix):
    infix = list(infix[::-1])  # Convert input string to a list of characters and reverse it
    l = len(infix)

    for i in range(l):
        if infix[i] == '(':
            infix[i] = ')'
        elif infix[i] == ')':
            infix[i] = '('

    postfix = infixToPostfix(''.join(infix))  # Join the characters back to a string before calling infixToPostfix
    prefix = ''.join(postfix[::-1])  # Convert postfix expression to prefix by reversing and joining the characters
    return prefix

# Rest of the code remains the same...

# Driver code
if __name__ == '__main__':
    s = "((A+B)*C-(D-E))^(F+G)"
    
    # Function call
    print(infixToPrefix(s))
