import pytest


ADD = 1
MULT = 2
EXIT = 99
ERR = -1

input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,6,19,23,1,23,5,27,1,27,13,
         31,2,6,31,35,1,5,35,39,1,39,10,43,2,6,43,47,1,47,5,51,1,51,9,55,2,55,
         6,59,1,59,10,63,2,63,9,67,1,67,5,71,1,71,5,75,2,75,6,79,1,5,79,83,1,
         10,83,87,2,13,87,91,1,10,91,95,2,13,95,99,1,99,9,103,1,5,103,107,1,
         107,10,111,1,111,5,115,1,115,6,119,1,119,10,123,1,123,10,127,2,127,13,
         131,1,13,131,135,1,135,10,139,2,139,6,143,1,143,9,147,2,147,6,151,1,5,
         151,155,1,9,155,159,2,159,6,163,1,163,2,167,1,10,167,0,99,2,14,0,0]

def get_op(op):
    if op == ADD:
        return lambda x, y: x + y
    if op == MULT:
        return lambda x, y: x * y
    if op == EXIT:
        return EXIT
    raise BaseException(op)


def handle(int_code, pos):
    op = get_op(int_code[pos])
    if op == EXIT:
        return False
    in1 = int_code[int_code[pos+1]]
    in2 = int_code[int_code[pos+2]]
    out_pos = int_code[pos+3]
    int_code[out_pos] = op(in1, in2)
    return True


def compute(int_code):
    pos = 0
    while handle(int_code, pos):
        pos += 4

    return int_code


@pytest.mark.parametrize("test_in,expected",
                         [([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
                          ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
                          ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
                          ([1, 1, 1, 4, 99, 5, 6, 0, 99],
                           [30, 1, 1, 4, 2, 5, 6, 0, 99])])
def test_compute(test_in, expected):
    res = compute(test_in)
    print(f'{res}, {expected}')
    assert res == expected, f'{res} != {expected}'


def init(int_code, noun=12, verb=2):
    """
    replace position 1 with the value 12
    and replace position 2 with the value 2
    """
    dup = int_code.copy()
    dup[1] = noun
    dup[2] = verb
    return dup


def search_noun_verb(search_input, output=19690720, nouns=range(100), verbs=range(100)):
    for noun in nouns:
        for verb in verbs:
            res = compute(init(search_input, noun, verb))
            if res[0] == output:
                return noun, verb
    raise BaseException("failed to find output")


def main():
    res = compute(init(input))
    print(f"Step 1: {res[0]}")
    noun, verb = search_noun_verb(input)
    print(f"Step 2: {100 * noun + verb}")


if __name__ == '__main__':
    main()
