import ast

class TypeChecker(ast.NodeVisitor):
    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        left_type = self.get_type(node.left)
        right_type = self.get_type(node.right)
        
        # Perform type checking for binary operations
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            if not (isinstance(left_type, (int, float)) and isinstance(right_type, (int, float))):
                print(f"Type error: operands {left_type} and {right_type} must be numeric for {node.op}")
    
    def visit_Name(self, node):
        # Simulate type lookup for names (variables)
        return int  # Simplified, assume all names are integers for this example
    
    def get_type(self, node):
        return self.visit(node)
    
# Example usage
def main():
    code = """
int a = 5
int b = 2
int c = a + b
"""   
    
    try:
        tree = ast.parse(code)
        TypeChecker().visit(tree)
    except SyntaxError as e:
        print(f"SyntaxError in code: {e}")

if __name__ == "__main__":
    main()
