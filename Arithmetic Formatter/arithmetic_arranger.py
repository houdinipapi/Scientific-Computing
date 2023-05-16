"""
Creating an arithmetic arranger program.
The function will return the correct conversion if the supplied problems are properly formatted, otherwise,
it will return a string that describes an error that is meaningful to the user.
"""


# Define the function --> Takes two arguments(list of strings, and a boolean)
def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems exceeds the limit of five.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize four empty lists: --> Will store the formatted components of each problem.
    top_nums = list()
    bottom_nums = list()
    lines = list()
    results = list()

    # Iterate over each problem in the 'problems' list.
    for problem in problems:
        # split each problem into its components --> first operand, operator, and second operand.
        first_operand, operator, second_operand = problem.split()

        # Check if the operator is valid.
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if both operands consist of digits only.
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the length of any operand exceeds four digits.
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the maximum length among the two operands and add two spaces to it --> width.
        width = max(len(first_operand), len(second_operand)) + 2

        # Add the formatted components of the problem to the respective lists.
        top_nums.append(first_operand.rjust(width))
        bottom_nums.append(operator + second_operand.rjust(width - 1))
        lines.append('-' * width)

        # If True --> calculate the answer based on the operator and the operands & Append it to 'results'.
        if show_answers:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))

            else:
                result = str(int(first_operand) - int(second_operand))

            results.append(result.rjust(width))

    # Final arranged string --> Joining the formatted components from the lists.
    arranged_problems = '    '.join(top_nums) + '\n' + '    '.join(bottom_nums) + '\n' + '    '.join(lines)

    # If True --> add a line containing the results.
    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    # Return the final arranged string.
    return arranged_problems
