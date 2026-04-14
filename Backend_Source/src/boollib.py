import sympy
from sympy.logic.boolalg import simplify_logic
import re

def advanced_parse(user_input):
    # 1. Standardize operators
    # Change + to | and * to &
    substitutions = {
        '+': '|',
        'v': '|',
        'u': '|',
        '*': '&',
        '^': '&',
        'n': '&',
        '!': '~'
    }

    processed = user_input
    for old, new in substitutions.items():
        processed = processed.replace(old, new)
    # 2. Handle standalone 1 and 0 (Finesse part)

    # \b[01]\b ensures we only catch 1 or 0 when they are NOT part of A1, B0, etc.
    processed = re.sub(r'\b1', ' T213769 &', processed)
    processed = re.sub(r'\b0', ' F213769 &', processed)

    # 3. Add implicit AND operators (The "AB" -> "A & B" logic)
    # This regex finds a variable and looks for another variable immediately following it.
    # It handles: AB -> A&B, A1B2 -> A1&B2, A(B) -> A&(B)
    processed = re.sub(r'(\b[a-zA-Z][a-zA-Z0-9]*\b)(?=\s*[a-zA-Z(])', r'\1 & ', processed)
    processed = re.sub(r'\)(?=\s*[a-zA-Z0-9])', r') & ', processed)
    processed = re.sub(r'\)(?=\s*\()', r') & ', processed)


    processed = re.sub(r'\bT213769\b', 'True ', processed)
    processed = re.sub(r'\bF213769\b', 'False ', processed)
    processed = re.sub(r'&&', '&', processed)
    processed = re.sub(r'&\|', '|', processed)
    # This will remove any trailing '&', '|', or spaces
    processed = processed.strip().rstrip('&|').strip()
    # 4. Detect symbols AFTER the implicit ANDs have been added
    # Now that 'AB' is 'A & B', this will find 'A' and 'B' separately
    symbols_found = set(re.findall(r'\b[a-zA-Z][a-zA-Z0-9]*\b', processed))
    
    # Remove logic keywords
    for kw in {'AND', 'OR', 'NOT', 'XOR', 'True', 'False'}:
        symbols_found.discard(kw)
    
    # 5. Create symbols and simplify
    sym_dict = {s: sympy.Symbol(s) for s in symbols_found}
    
    try:
        # sympify handles the parentheses and logic
        expr = sympy.sympify(processed, locals=sym_dict)
        simplified = simplify_logic(expr)
        
        print("\n" + "="*30)
        print(f"Processed Logic:   {processed}")
        print(f"Detected Variables: {sorted(list(symbols_found))}")
        print(f"Simplified Result:  {simplified}")
        print("="*30)
        
    except Exception as e:
        print(f"Error: Could not parse. {e}")

if __name__ == "__main__":
    while True:
        test_input = input("Enter equation (or 'stop' to exit): ")
        if test_input == "stop":
            break
        advanced_parse(test_input)