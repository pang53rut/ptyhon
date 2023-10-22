import java.util.Stack;

public class InfixToPrefix {
    private static int getPrecedence(char ch) {
        switch (ch) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
        }
        return -1;
    }

    public static String infixToPrefix(String infix) {
        StringBuilder prefix = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        Stack<String> operands = new Stack<>();

        for (char ch : new StringBuilder(infix).reverse().toString().toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                operands.push(String.valueOf(ch));
            } else if (ch == ')') {
                stack.push(ch);
            } else if (ch == '(') {
                while (!stack.isEmpty() && stack.peek() != ')') {
                    operands.push(stack.pop().toString());
                }
                stack.pop(); // Pop ')'
            } else {
                while (!stack.isEmpty() && getPrecedence(ch) < getPrecedence(stack.peek())) {
                    operands.push(stack.pop().toString());
                }
                stack.push(ch);
            }
        }

        while (!stack.isEmpty()) {
            operands.push(stack.pop().toString());
        }

        while (!operands.isEmpty()) {
            prefix.append(operands.pop());
        }

        return prefix.reverse().toString();
    }

    public static void main(String[] args) {
        String infixExpression = "(A+B)*C-D/(E+F)";
        String prefixExpression = infixToPrefix(infixExpression);
        System.out.println("Prefix Expression: " + prefixExpression);
    }
}
