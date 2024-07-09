import re
import sys

# Define regular expressions for some MISRA C rules
RULES = {
    "Rule 1.1": re.compile(r'[^ -~\t\n\r]'),  # Non-printable ASCII characters
    "Rule 2.1": re.compile(r'unreachable_code'),  # Simplified check for unreachable code
    "Rule 3.1": re.compile(r'[^\x20-\x7E\t\n\r]'),  # Non-ASCII characters
    "Rule 5.1": re.compile(r'\b[A-Za-z_]\w{31,}\b'),  # Identifier length exceeding 31 characters
    "Rule 6.1": re.compile(r'\bstruct\b.*\b:\s*(?!\b(int|unsigned int|signed int|_Bool)\b)'),  # Invalid bit-field types
    "Rule 7.1": re.compile(r'\b0[0-7]+\b'),  # Octal constants
    "Rule 8.1": re.compile(r'\b[A-Za-z_]\w*\s*\([^)]*\)\s*{'),  # Function prototype
    "Rule 8.2": re.compile(r'\bextern\b\s+.*\b=\s*'),  # External linkage with definition
    "Rule 9.1": re.compile(r'\b[A-Za-z_]\w*\s+([A-Za-z_]\w*)\s*;'),  # Uninitialized variable
    "Rule 10.1": re.compile(r'[\+\-\*/%]=|=[\+\-\*/%]|==|!=|<=|>=|&&|\|\|'),  # Complex expressions
    "Rule 11.1": re.compile(r'\(\s*(void|char|short|long|float|double|int)\s*\*\s*\)'),  # Type conversions
    "Rule 12.1": re.compile(r'\bif\s*\([^)]*\)|\bwhile\s*\([^)]*\)|\bfor\s*\([^)]*\)'),  # Operator precedence
    "Rule 14.1": re.compile(r'\b(atof|atoi|atol|atoll)\s*\('),  # Standard library functions
    "Rule 15.1": re.compile(r'\bgoto\b'),  # Use of goto
    "Rule 16.1": re.compile(r'\bcontinue\b'),  # Use of continue
    "Rule 17.1": re.compile(r'#\s*define\s+\w+\s*\('),  # Macro definitions
    "Rule 17.2": re.compile(r'\b(int|char|float|double|short|long)\b'),  # Use of basic numerical types
    "Rule 18.1": re.compile(r'\b(double|float)\b'),  # Floating-point numbers
    "Rule 19.1": re.compile(r'\b([A-Za-z_]\w*)\s*=\s*[^;]*\b([A-Za-z_]\w*)\b'),  # Implicit conversions
    "Rule 19.2": re.compile(r'\bunion\b'),  # Use of union types
    "Rule 20.1": re.compile(r'\bfor\s*\([^;]*;[^;]*;[^)]*\)'),  # Non-constant loop conditions
    "Rule 21.1": re.compile(r'\b\*\s*(\+\+|--|\+|\-|\*)'),  # Pointer arithmetic
    "Rule 2.3": re.compile(r'//'),  # Use of C++ style comments
    "Rule 12.2": re.compile(r'\bif\s*\(.*?&&.*?\)|\bwhile\s*\(.*?&&.*?\)|\bfor\s*\(.*?&&.*?\)'),  # More complex expressions in control flow
    "Rule 13.1": re.compile(r'&(?![a-zA-Z0-9])'),  # Misuse of bitwise operators
    "Rule 14.3": re.compile(r'\belse\s+if\b'),  # Misuse of else-if
    "Rule 15.4": re.compile(r'\bbreak\b'),  # Misuse of break
    "Rule 20.3": re.compile(r'\bfor\s*\([^;]*;[^;]*;[^)]*\)\s*{[^}]*\bbreak\b'),  # Misuse of break in loops
    "Rule 21.3": re.compile(r'\bvoid\s*\*\b'),  # Use of void pointers
    "Rule 22.2": re.compile(r'assert\s*\('),  # Use of assert macro
}

def check_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    violations = []
    for rule, pattern in RULES.items():
        if pattern.search(content):
            violations.append(rule)

    return violations

def main():
    if len(sys.argv) < 2:
        print("Usage: python misra_checker.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    violations = check_file(filename)

    if violations:
        print(f"Violations found in {filename}:")
        for violation in violations:
            print(f" - {violation}")
    else:
        print(f"No violations found in {filename}.")

if __name__ == "__main__":
    main()
