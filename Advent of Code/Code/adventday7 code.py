def merge_numbers(a, b):
    return int(str(a) + str(b))

def can_make_equation(target, numbers):
    from itertools import product
    
    operators = ['+', '*', '||']
    num_slots = len(numbers) - 1
    all_possible_ops = product(operators, repeat=num_slots)
    
    for ops in all_possible_ops:
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            elif op == '||':
                result = merge_numbers(result, numbers[i + 1])
        if result == target:
            return True
    return False

fullFile = []
valid_equations = []
valid_targets = []

with open(r"C:\Users\Msb12\OneDrive - Regis Jesuit High School\Desktop\Advent-of-Code\Advent of Code\.txt documents\adventday7.txt", "r") as file:
    for line in file:
        line = line.strip()
        if ":" in line:
            target_str, numbers_str = line.split(":")
            target = int(target_str)
            numbers = [int(x) for x in numbers_str.split()]
            
            if can_make_equation(target, numbers):
                valid_targets.append(target)
                valid_equations.append(line)
                print(f"Found valid equation: {line}") #I was wondering if it was working because it was taking a bit longer than I expected, so this tracks each found one

print(f"There are {len(valid_equations)} valid equations")
print(f"Sum of valid target values: {sum(valid_targets)}")

