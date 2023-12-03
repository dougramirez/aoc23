from collections import OrderedDict

calibration_values = list()
calibration_values_sum = 0


number_strings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Open the calibration document
calibration_document = open("./day1/calibration_document.txt", "r")


def find_digits(string: str) -> str:
    locations = OrderedDict()

    # Find all the instances of numbers spelled out with letters in the string
    for number in number_strings:
        start = 0
        while True:
            location = line.find(number, start)
            if location >= 0:
                # Keep track of the spelled out number and its location in the string
                locations.update({location: number})
                start = location + len(number)
            else:
                break

    # Find all the instances of numbers in the string
    for number in numbers:
        start = 0
        while True:
            location = line.find(number, start)
            if location >= 0:
                # Keep track of the number and its location in the string
                locations.update({location: number})
                start = location + len(number)
            else:
                break

    # Sort the locations so we know which number or number spelled out is first
    locations = OrderedDict(sorted(locations.items(), key=lambda t: t[0]))

    first = locations[next(iter(locations))]
    if first.isdigit():
        first_digit = first
    else:
        first_digit = number_strings[first]

    last = locations[next(reversed(locations))]
    if last.isdigit():
        last_digit = last
    else:
        last_digit = number_strings[last]

    calibration_value = int(f"{first_digit}{last_digit}")

    return calibration_value


for line in calibration_document:
    line = line.strip()
    calibration_value = find_digits(line)
    calibration_values.append(calibration_value)

for value in calibration_values:
    calibration_values_sum += value

print(f"\nSum of all the calibration values is: {calibration_values_sum}")
