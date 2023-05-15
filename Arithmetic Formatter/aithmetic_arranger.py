def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_nums = list()
    bottom_nums = list()
    lines = list()
    results = list()

    for problem in problems:
        first_operand, operator, second_operand = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(first_operand), len(second_operand)) + 2
        top_nums.append(first_operand.rjust(width))
        bottom_nums.append(operator + second_operand.rjust(width - 1))
        lines.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))

            else:
                result = str(int(first_operand) - int(second_operand))

            results.append(result.rjust(width))

    arranged_problems = '    '.join(top_nums) + '\n' + '    '.join(bottom_nums) + '\n' + '    '.join(lines)

    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
