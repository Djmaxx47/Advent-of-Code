import re

def detect_and_compute_mul_from_file(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    mul_pattern = r'mul\((\d+),\s*(\d+)\)'
    #also had to look the syntax for filtering results up
    mul_values = re.findall(mul_pattern, text)

    results = []
    for value in mul_values:
        a, b = map(int, value)
        result = a * b
        results.append((a, b, result))

    final_result = sum(result for _, _, result in results)
    #I had to look this part up, I had no clue how to get all of the results together.
    return results, final_result

file_name = 'adventday3.txt'
results, final_result = detect_and_compute_mul_from_file(file_name)
print(f"Final result: {final_result}")
