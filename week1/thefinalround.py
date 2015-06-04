from therealdeal import to_number
from warmup import sum_of_digits
from math import floor


def count_words(arr):
    result = {}
    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def unique_words_count(arr):
    return len(count_words(arr))


def nan_expand(times):
    if times == 0:
        return ""
    result = ""
    n = "Not a "
    for time in range(1, times+1):
        result += n
    result += "Nan"
    return result


def iteration_of_nan_expand(expanded):
    if expanded == "":
        return 0
    if expanded.count("Not a Nan") == 0:
        return False
    else:
        return expanded.count("Not a")


def is_prime(n):
    if n <= 1:
        return False

    start = 2

    while start < n:
        if n % start == 0:
            return False

        start += 1

    return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


def divide_count(n, k):
    times = 0

    while n != 1 and n % k == 0:
        times += 1
        n = n//k

    return times


def prime_factorization(n):
    result = []

    current_prime = 2

    while n != 1:
        times = divide_count(n, current_prime)

        if times != 0:
            result.append((current_prime, times))
            n = n//current_prime ** times

        current_prime = next_prime(current_prime)

    return result


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and first == items[index]:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def group_by(func, seq):
    result = {}
    for element in seq:
        if func(element) in result:
            result[func(element)].append(element)
        else:
            result[func(element)] = [element]
    return result


def prepare_meal(number):
    result = ""
    sp = "spam "
    while number % 3 == 0:
        result += sp
        number = number//3

    if number % 5 == 0:
        result += "and eggs"
        number = number//5
    return result


def reduce_file_path(path):
    result = []
    parts = [part for part in path.split("/") if part not in [".", ""]]

    while len(parts) != 0:
        part = parts.pop()

        if part == "..":
            if len(parts) != 0:
                parts.pop()
        else:
            result.insert(0, part)

    return "/" + "/".join(result)


def is_an_bn(word):
    return word.count("a") == word.count("b")


def to_digits(n):
    return [int(x) for x in str(n)]


def transform_number(number):
    num = str(number)[::-1]
    result = []
    for i in range(0, len(num)):
        if i % 2 != 0:
            result.append(int(num[i]) * 2)
        else:
            result.append(int(num[i]))
    return to_number(result)


def is_credit_card_valid(number):
    return sum_of_digits(transform_number(number)) % 10 == 0


def goldbach(n):
    result = []
    current_prime = 2
    new = n - current_prime
    if is_prime(new):
        result.append((new, current_prime))
    current_prime = next_prime(current_prime)

    return result


def which_year(year):
    is_leap = False
    first_day = 0
    if year % 4 == 0 and year % 100 != 0:
        is_leap = True
    century = (year // 100) % 4
    if century == 0:
        century = 6
    elif century == 1:
        century = 4
    elif century == 2:
        century = 2
    else:
        century = 0
    if is_leap:
        first_day = 7 + century + year % 100 + floor((year % 100) / 4)
    else:
        first_day = 1 + century + year % 100 + floor((year % 100) / 4)
    first_day = first_day % 7
    return first_day


def friday_years(year1, year2):
    result = 0
    for year in range(year1, year2 + 1):
        which = which_year(year)

        is_leap = False
        if year % 4 == 0 and year % 100 != 0:
            is_leap = True
        if (which == 4 and is_leap == True) or which == 5:
            result += 1

    return result

print(friday_years(1000, 2000))