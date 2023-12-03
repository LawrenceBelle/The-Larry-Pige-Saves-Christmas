
from day_1.big_string import really_big_string

NUMBERS_AS_STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
NUMBERS_AS_STRINGS_BACKWARDS = [num[::-1] for num in NUMBERS_AS_STRINGS]

def get_value(input: str) -> int:
    sum = 0
    split_input = input.split('\n')

    for line in split_input:
        line_backwards = line[::-1]
        calibration_thing = ''

        print(line)
        first_int_index, first_int = find_first_int_instance_index(line)
        first_string_index, first_string = find_first_text_instance_index(line, NUMBERS_AS_STRINGS)

        print("\nbackwards:", line_backwards)
        last_int_index, last_int = find_first_int_instance_index(line_backwards)
        last_string_index, last_string = find_first_text_instance_index(line_backwards, NUMBERS_AS_STRINGS_BACKWARDS)

        if first_int_index < first_string_index:
            calibration_thing += first_int
        else:
            calibration_thing += first_string

        if last_int_index < last_string_index:
            calibration_thing += last_int
        else:
            calibration_thing += last_string

        print(calibration_thing, "\n")

        sum += int(calibration_thing)

    return sum


def find_first_int_instance_index(input: str) -> (int, str):
    value = next(char for char in input if char.isdecimal())
    index = input.index(value)

    print("int index", index)

    return index, value


def find_first_text_instance_index(input: str, string_numbers: list[str]) -> (int, str):
    first_instances = list(map(input.find, string_numbers))

    valid_first_instances = [i for i in first_instances if i >= 0]

    if valid_first_instances == []:
        return 999999, ""

    first_first_instance = min([i for i in first_instances if i >= 0])

    value = first_instances.index(first_first_instance) + 1

    index = first_first_instance

    print("string index", index)

    return index, str(value)


if __name__ == '__main__':
    print("sum:", get_value(really_big_string))