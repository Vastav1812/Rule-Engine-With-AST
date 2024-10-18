class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # Can be 'operator' or 'operand'
        self.value = value  # The actual condition (e.g., 'age > 30')
        self.left = left  # Left child for operator nodes
        self.right = right  # Right child for operator nodes

# Function to create AST from rule string
def create_rule(rule_string):
    # Split based on AND or OR first to manage conditions properly
    if ' AND ' in rule_string:
        parts = rule_string.split(' AND ')
        left_part = create_rule(parts[0].strip())  # Recursive call to create AST
        right_part = create_rule(parts[1].strip())
        return Node('operator', 'AND', left_part, right_part)
    elif ' OR ' in rule_string:
        parts = rule_string.split(' OR ')
        left_part = create_rule(parts[0].strip())
        right_part = create_rule(parts[1].strip())
        return Node('operator', 'OR', left_part, right_part)
    else:
        # Handle individual conditions, assume conditions are in format "attribute <value>"
        return Node('operand', rule_string.strip())

# Function to combine ASTs
def combine_rules(asts, operator):
    combined_ast = asts[0]
    for ast in asts[1:]:
        combined_ast = Node('operator', operator, combined_ast, ast)
    return combined_ast

# Function to evaluate user data against the AST
# Function to evaluate user data against the AST
# Function to evaluate user data against the AST
def evaluate_rule(node, user_data):
    print(f"Evaluating node: {node.node_type}, value: {node.value}")
    if node.node_type == 'operator':
        print(f"Evaluating operator: {node.value}")
        if node.value == 'AND':
            left_result = evaluate_rule(node.left, user_data)
            right_result = evaluate_rule(node.right, user_data)
            print(f"AND evaluation: left={left_result}, right={right_result}")
            return left_result and right_result
        elif node.value == 'OR':
            left_result = evaluate_rule(node.left, user_data)
            right_result = evaluate_rule(node.right, user_data)
            print(f"OR evaluation: left={left_result}, right={right_result}")
            return left_result or right_result
    elif node.node_type == 'operand':
        condition = node.value.strip()
        print(f"Evaluating condition: {condition}")

        if '>' in condition:
            attribute, value = condition.split('>')
            attribute = attribute.strip()
            value = int(value.strip())
            print(f"Condition: {attribute} > {value}, user_data: {user_data.get(attribute)}")
            result = user_data.get(attribute, 0) > value
            print(f"Result: {result}")
            return result
        elif '=' in condition:
            attribute, value = condition.split('=')
            attribute = attribute.strip()
            value = value.strip().strip("'").strip('"')  # Strip both single and double quotes
            print(f"Condition: {attribute} = {value}, user_data: {user_data.get(attribute)}")
            result = user_data.get(attribute) == value
            print(f"Result: {result}")
            return result