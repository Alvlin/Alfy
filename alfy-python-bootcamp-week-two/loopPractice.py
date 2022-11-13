import math

def input_list():
    num = input("")
    vals = []
    sum = 0
    while num != "":
        try:
            sum += int(num)
            vals.append(int(num))
            num = input("")
        except:
            num = input("")
    vals.append(int(sum))
    return vals


def check_monotonic_sequence(sequence):
    if not sequence or len(sequence) == 1:
         return [True, True, True, True]

    prev_check = None
    prev = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        curr = sequence[i]
        check = gle(prev, curr)
        if prev_check is None:
            prev_check = check
        elif check == 0:
            prev = curr
            continue
        elif check != prev_check:
            return [False, False, False, False]
        prev = curr
        count += 1
    if prev_check == 0:
        return [True, False, True, False]
    elif prev_check == -1:
        if count == len(sequence):
            return [True, True, False, False]
        else:
            return [True, False, False, False]
    else:
        if count == len(sequence):
            return [False, False, True, True]
        else:
            return [False, False, True, False]


def gle(prev, curr):
    if prev < curr:
        return -1
    if prev == curr:
        return 0
    if prev > curr:
        return 1


def check_monotonic_sequence_inverse(def_bool):
    match def_bool:
        case [True, True, False, False]:
            return [1, 2, 3, 4, 5, 6, 7, 8]
        case [True, False, False, False]:
            return [1, 2, 2, 3]
        case [True, False, True, False]:
            return [1, 1, 1, 1]
        case [False, False, True, False]:
            return [3, 2, 1, 1]
        case [False, False, True, True]:
            return [7.5, 4, 3.141, 0.111]
        case [False, False, False, False]:
            return [1, 0, -1, 1]
        case [True, True, True, True]:
            return []
        case _:
            return None


def primes_generator(n):
    primes = []
    start = 2
    while len(primes) < n:
        if check_prime(start):
            primes.append(start)
        start += 1
    return primes


def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_empty_vector(vec_lst):
    if not vec_lst:
        return True
    return False


def vectors_list_sum(vec_lst):
    if is_empty_vector(vec_lst) or not vectors_even_len(vec_lst):
        return 0
    fin_vec = vec_lst[0]
    for i in range(1, len(vec_lst)):
        fin_vec = [a+b for a, b in zip(fin_vec, vec_lst[i])]
    return fin_vec


def vectors_even_len(vec_lst):
    size = len(vec_lst[0])
    for vec in vec_lst:
        if len(vec) != size:
            return False
    return True


def calc_the_inner_product(vec_1, vec_2):
    if not vec_1 and not vec_2:
        return 0
    elif not vec_1 or not vec_2:
        return None
    return sum([a*b for a, b in zip(vec_1, vec_2)])


def orthogonal_number(vectors):
    ortho = 0
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            ortho += 1 if calc_the_inner_product(vectors[i],vectors[j]) == 0 else 0
    return ortho

calc_the_inner_product([], [1])