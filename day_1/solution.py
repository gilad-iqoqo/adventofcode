import math
import pytest


def to_fuel(mod_weight):
    return max(math.floor(int(mod_weight)/3) - 2, 0)


@pytest.mark.parametrize("test_in,expected",
                         [("12", 2),
                          ("14", 2),
                          ("1969", 654),
                          ("100756", 33583)])
def test_to_fuel(test_in, expected):
    assert to_fuel(test_in) == expected


@pytest.mark.parametrize("test_in,expected", [("1969", 966), ("100756", 50346)])
def test_fuels_of_fuels(test_in, expected):
    fuels = [to_fuel(test_in)]
    assert fuels_of_fuels(fuels) == expected


def modules_fuel():
    with open('input', 'r') as f:
        fuels = [to_fuel(ll) for ll in f.readlines()]

    print(f"PART 1: modules fuel = {sum(fuels)}")
    return fuels


def fuels_of_fuels(fuels):
    total = 0
    while sum(fuels) > 0:
        total += sum(fuels)
        fuels = [to_fuel(x) for x in fuels]

    print(f"PART 2: total fuel = {total}")
    return total


def main():
    fuels = modules_fuel()
    fuels_of_fuels(fuels)


if __name__ == '__main__':
    main()
