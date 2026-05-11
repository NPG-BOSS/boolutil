import sympy as sp
from sympy.logic.boolalg import simplify_logic, And, Or, Not, Nand, truth_table
import re


class Expression:
    def __init__(self, plaintext = None, ttable = None, sympy_expr = None):
        if plaintext is not None:
            self.plaintext = plaintext
            self.sympy_expr = text_to_logic(plaintext)
            self.ttable = truth_table(self.sympy_expr, self.sympy_expr.atoms(sp.Symbol))
            self.ttable_readable = list(self.ttable)





def text_to_logic(plaintext_expression):
    """
    Converts plaintext logic expressions into a format that can be processed by sympy, and extracts symbols as sympy Symbols.

    Inputs:
    - plaintext_expression: A string containing the logic expression in plaintext format.
    - Allowed symbols for logic operations include:
        - OR: +, v, u, OR, |
        - AND: *, n, AND, & 
        - NOT: !, NOT, ~
        - True: 1, True (trailing 1 will be treated as a symbol unsless explicid logic operator is used before it)
        - False: 0, False (trailing 1 will be treated as a symbol unsless explicid logic operator is used before it)
    -Allowed variable names:
        - 1 large or small letter followed by any amount of numbers
        - expection, names starting with v, u, n ;
         and logic operaotrs
    Outputs:
    - processed: A string with the logic expression converted to sympy format.
    """
    # Change different logic symbols to format accepted by sympy
    substitutions = {
        '+': '|',
        'v': '|',
        'u': '|',
        'OR': '|',
        '*': '&',
        'n': '&',
        'AND': '&',
        '!': '~',
        'NOT': '~',
        'XOR': '^'
    }

    processed = plaintext_expression
    for old, new in substitutions.items():
        processed = processed.replace(old, new)


    # Pre process leading 1 and 0 to custom tags to later change to True and False
    # If changed right to True and False, it would treat each letter as a symbol

    processed = re.sub(r'\b1', ' T213769 &', processed)
    processed = re.sub(r'\b0', ' F213769 &', processed)

    # Split symbols directly next to each other and add an implicit AND between them
    processed = re.sub(r'([a-zA-Z0-9])(?=[a-zA-Z(~])', r'\1 & ', processed)
    #Handle parentheses
    processed = re.sub(r'\)(?=\s*[a-zA-Z0-9])', r') & ', processed)
    processed = re.sub(r'\)(?=\s*\()', r') & ', processed)

    # Replace the custom tags with True and False
    processed = re.sub(r'\bT213769\b', 'True ', processed)
    processed = re.sub(r'\bF213769\b', 'False ', processed)

    # Handle double and trailing operators
    processed = re.sub(r'&&', '&', processed)
    processed = re.sub(r'&\|', '|', processed)
    processed = processed.strip().rstrip('&|').strip()


    # Detect symbols (variables) in the processed expression
    symbols_found = set(re.findall(r'\b[a-zA-Z][a-zA-Z0-9]*\b', processed))
    keywords = {'AND', 'OR', 'NOT', 'XOR', 'v', 'True', 'False'}
    symbols_found = {s for s in symbols_found if s not in keywords}
    sym_dict = {s: sp.Symbol(s) for s in symbols_found}

    sympy_expr = sp.sympify(processed, locals=sym_dict)

    return sympy_expr

    
def simplify_expression(expression):
    """Simplification of logic taken straight from sympy. mostly for having single namespace when using library"""
 
    try:
        simplified = simplify_logic(expression)
        return simplified
    except Exception as e:
            print(f"Error simplifying expression: {e}")
            return None 

def logic_to_nand_style(expr):
    # 1. Base Case: If it's a variable, we're done
    if expr.is_Atom:
        return expr

    # 2. Check for Double Negation: ~(~A) -> A
    # If the current gate is a NOT and the child is also a NOT, skip both
    if isinstance(expr, Not) and isinstance(expr.args[0], Not):
        return logic_to_nand_style(expr.args[0].args[0])

    # 3. Recursively convert all child arguments
    args = [logic_to_nand_style(arg) for arg in expr.args]

    # Helper: Visual NAND gate ~(A & B)
    def NAND_GATE(*inputs):
        return Not(And(*inputs, evaluate=False), evaluate=False)

    # 4. NAND Mapping
    if isinstance(expr, Not):
        return Not(args[0])

    if isinstance(expr, And):
        inner = NAND_GATE(*args)
        return NAND_GATE(inner, inner)

    if isinstance(expr, Or):
        not_args = [Not(a) for a in args]
        return Nand(*not_args)

    return expr    

if __name__ == "__main__":

    while True:
        test_input = input("Enter equation (or 'stop' to exit): ")
        if test_input == "stop":
            break
        processed = text_to_logic(test_input)
        a = Expression(plaintext=test_input)
        print(a.ttable_readable)


        print(f"Processed: {processed}")
        processed = simplify_expression(processed)
        print(f"Simplified: {processed}")
        processed = logic_to_nand_style(processed)
        print(f"Nandified: {processed}")