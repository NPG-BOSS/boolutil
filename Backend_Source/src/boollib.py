import sympy as sp
from sympy.logic.boolalg import simplify_logic, And, Or, Not, Nand
import re

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

    return processed

    
def simplify_expression(expression):
    """Simplification of logic taken straight from sympy. mostly for having single namespace when using library"""
 
    try:
        simplified = simplify_logic(expression)
        return simplified
    except Exception as e:
            print(f"Error simplifying expression: {e}")
            return None 

def logic_to_nand_form(expression):
    """
    Converts expression to form which can be implemented using only NAND gates.
    It checks top level operator, changes it to nand form and then recursively calls itself on the arguments of the operator.
    """
    if expression.is_Atom:
        return expression

    if isinstance(expression, Not):
        a = logic_to_nand_form(expression.args[0])
        return Nand(a, a)

    if isinstance(expression, Or):
        args = list(expression.args)
        #expr = binarize(Or, args)
        a, b = expression.args
        a, b = logic_to_nand_form(a), logic_to_nand_form(b)
        return Nand(Nand(a, a), Nand(b, b))

    if isinstance(expression, And):
        args = list(expression.args)
        #expr = binarize(And, args)
        a, b = expression.args
        a, b = logic_to_nand_form(a), logic_to_nand_form(b)
        t = Nand(a, b)
        return Nand(t, t)

    raise ValueError(expression)    

if __name__ == "__main__":

    while True:
        test_input = input("Enter equation (or 'stop' to exit): ")
        if test_input == "stop":
            break
        processed = text_to_logic(test_input)
        

        print(f"Processed: {processed}")
        processed = simplify_expression(processed)
        print(f"Simplified: {processed}")
        processed = logic_to_nand_form(processed)
        print(f"Nandified: {processed}")