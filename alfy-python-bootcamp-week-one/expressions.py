from expressions import *
import math


def calc_math_expression(num1, num2, operator):
    try:
        match operator:
            case '+':
                return float(num1) + float(num2)
            case '-':
                return float(num1) - float(num2)
            case '*':
                return float(num1) * float(num2)
            case ':':
                if num2 == 0:
                    return "Can't Divide by 0"
                else:
                    return round(int(num1) / int(num2), 2)
        return None
    except:
        return None


def calc_math_expression_from_str(str_input):
    expression = str_input.split(" ")
    return calc_math_expression(expression[0], expression[2], expression[1])


def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    return max(num1, num2, num3), min(num1, num2, num3)


def quadratic_equation_solver(a, b, c):
    try:
        sqrtme = (b * b) - (4 * a * c)
        x = (-b + math.sqrt(sqrtme)) / (2 * a)
        x2 = (-b - math.sqrt(sqrtme)) / (2 * a)

        if x != x2:
            return x, x2
        else:
            return x, None
    except:
        return None, None


def quadratic_equation_solver_from_user_input():
    try:
        val = str(input("Enter a, b, c values")).split(" ")
        return quadratic_equation_solver(val[0], val[1], val[2])
    except:
        return None


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    temps = [temp_1, temp_2, temp_3]
    count = 0
    for i in temps:
        if min_temp < i:
            count += 1
    return True if count >= 2 else False

assert calc_math_expression_from_str("10 : 2") == 5.0
assert calc_math_expression_from_str("10 : -2") == -5.0
assert calc_math_expression_from_str("-10 : -2") == 5.0
assert calc_math_expression_from_str("-10 : 2") == -5.0
assert calc_math_expression_from_str("10 + 2") == 12.0
assert calc_math_expression_from_str("100 - 39.3") == 60.7
assert calc_math_expression_from_str("5 : 2") == 2.5
assert calc_math_expression_from_str("5 : 0") is None
assert calc_math_expression_from_str("10 333 2") is None
assert calc_math_expression_from_str("10 ^ 2") is None


assert find_largest_and_smallest_numbers(5, 1, 10) == (10, 1)
assert find_largest_and_smallest_numbers(2.5, 2.5, 7) == (7, 2.5)
assert find_largest_and_smallest_numbers(7, 2.5, 2.5) == (7, 2.5)
assert find_largest_and_smallest_numbers(-5, -5, -5) == (-5, -5)
assert find_largest_and_smallest_numbers(10, -1, 10) == (10, -1)
assert find_largest_and_smallest_numbers(-2, 5, -2) == (5, -2)
assert find_largest_and_smallest_numbers(3, 20, -2) == (20, -2)
assert find_largest_and_smallest_numbers(7, 10, 0) == (10, 0)
assert find_largest_and_smallest_numbers(10, 7, 0) == (10, 0)
assert find_largest_and_smallest_numbers(0, 10.01, 10) == (10.01, 0)

assert quadratic_equation_solver(1, 1.5, -1) == (0.5, -2)
assert quadratic_equation_solver(1, -8, 16) == (4, None)
assert quadratic_equation_solver(1, -2, 34.5) == (None, None)
assert quadratic_equation_solver(4, -12, 9) == (3/2, None)


assert temp_checker(26, 38, 90, 20) is True
assert temp_checker(10, 10, 10, 10) is False
assert temp_checker(10, 11, 10, 11) is True
assert temp_checker(-1, -9, 0, 1) is True
assert temp_checker(0, 90, 0, 1) is True

print("All tests passed")