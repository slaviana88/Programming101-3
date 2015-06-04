import copy
import pprint


def sum_of_divisors(n):
    sum = 0
    for x in range(1, n+1):
        if n % x == 0:
            sum += x
    return sum


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def prime_number_of_divisors(n):
    count = 0
    for x in range(1, n+1):
        if n % x == 0:
            count += 1
    return is_prime(count)


def contains_digit(number, digit):
    if str(digit) in str(number):
        return True
    else:
        return False


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
    return True


def to_digits(n):
    return [int(x) for x in str(n)]


def is_balanced(n):
    numbs = to_digits(n)
    half = len(numbs) // 2
    left_n = numbs[0: half]
    if len(numbs) % 2 == 0:
        right_n = numbs[half:]
    else:
        right_n = numbs[half+1:]

    return sum(left_n) == sum(right_n)


def count_substrings(haystack, needle):
    return haystack.count(needle)


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def zero_insertion(n):
    result = []
    digits = to_digits(n)

    start = 0
    end = len(digits)

    while start < end-1:
        x = digits[start]
        y = digits[start+1]
        result.append(x)

        if(x+y) % 10 == 0 or x == y:
            result.append(0)

        start += 1
    result.append(digits[start])
    return to_number(result)


def sum_matrix(matr):
    result = 0
    for row in matr:
        result += sum(row)
    return result

NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            # This min() is not to go less than zero
            m[position[dx]][position[dy]] -= min(target_value, position_value)

    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == '__main__':
    main()