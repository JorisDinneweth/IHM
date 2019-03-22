import numpy as np


def random_draft():
    figures = list(range(1, 11))
    figures.extend([25, 50, 75, 100])
    draft = []

    while len(draft) < 6:
        n = np.random.choice(figures)
        if (n >= 25 and n not in draft) or (n <= 10 and draft.count(n) < 2):
            draft.append(n)

    return draft


def random_number():
    draft = random_draft()
    tmp_numbers = draft[:]
    operators = ['+', '-', '/', '*']
    solution = []

    while len(solution) < 5 or not(200 < tmp_numbers[-1] < 1000) or tmp_numbers[-1] % 5 == 0:
        tmp_numbers = draft[:]
        solution = []

        while len(tmp_numbers) > 1:
            # take two rand numbers and one operator
            n1, n2 = np.random.choice(tmp_numbers, size=2, replace=False)
            operator = np.random.choice(operators)

            # if operations are corrects -> append them into the solution list
            # else -> exit while
            if operator == '/':
                if n1 > n2 != 1 and n1 / n2 == n1 // n2 and (n1 // n2) not in tmp_numbers:
                    solution.append([n1, '/', n2])
                    tmp_numbers.append(n1 // n2)
                elif n2 > n1 != 1 and n2 / n1 == n2 // n1 and (n2 // n1) not in tmp_numbers:
                    solution.append([n2, '/', n1])
                    tmp_numbers.append(n2 // n1)
                else:
                    break
            elif operator == '-':
                if n2 > n1 and (n2 - n1) not in tmp_numbers:
                    solution.append([n2, '-', n1])
                    tmp_numbers.append(n2 - n1)
                elif n1 > n2 and (n1 - n2) not in tmp_numbers:
                    solution.append([n1, '-', n2])
                    tmp_numbers.append(n1 - n2)
                else:
                    break
            elif operator == '+' and (n2 + n1) not in tmp_numbers:
                solution.append([n2, '+', n1])
                tmp_numbers.append(n2 + n1)
            elif operator == '*' and n1 != 1 and n2 != 1 and (n2 * n1) not in tmp_numbers and (n2 * n1) < 1200:
                solution.append([n2, '*', n1])
                tmp_numbers.append(n2 * n1)
            else:
                break

            tmp_numbers.remove(n1)
            tmp_numbers.remove(n2)

    # return numbers, total, solution
    return draft, tmp_numbers[-1], [[str(elt) for elt in op] for op in solution]
