
from big_string import really_big_string

def get_value(input: str) -> int:
    sum = 0
    split_input = input.split('\n')
    for line in split_input:
        sum += int(f'{find_first_instance(line)}{find_first_instance(line[::-1])}')

    return sum


def find_first_instance(input: str) -> str:
    return next(char for char in input if char.isdecimal())


if __name__ == '__main__':
    print(get_value(really_big_string))