symbols = ["*", "/", "@", "&", "#", "$", "+", "%", "=", "-"]

# Open the engine schematic and load into an array of strings
engine_schematic = open("./day3/engine_schematic.txt", "r")
engine_schematic_array = []
line_number = 1
for line in engine_schematic:
    line = line.strip()
    engine_schematic_array.append([line_number, line])
    line_number += 1


def is_part_number(look_locations):
    for location in look_locations:
        number = int(location[0])
        line_number = int(location[1]) - 1
        position = location[2]

        # We need to figure out this off by 1 bug
        if position < 140:
            char = engine_schematic_array[line_number][1][position]
            if char in symbols:
                print(f"{number} is a part number\n")

                return True

    print(f"{number} is NOT a part number\n")

    return False


def where_to_look(number, line_number, start, end):
    look_locations = list()

    # Look left
    char_left_of_number = ""
    if start > 0:
        left_of_number = start - 1
        look_locations.append([number, line_number, left_of_number])
        char_left_of_number = engine_schematic_array[line_number - 1][1][
            look_locations[0][2]
        ]

    # Look right
    char_right_of_number = ""
    if end < 140:
        right_of_number = end + 1
        look_locations.append([number, line_number, right_of_number - 1])
        char_right_of_number = engine_schematic_array[line_number - 1][1][
            right_of_number - 1
        ]

    # Look up
    look_up_locations = list()
    if line_number > 1:
        # We need to handle the condition when this number is as the beginning
        # of the line
        if start < 1:
            start = 1
        for i in range(start - 1, end + 1):
            look_up_locations.append([number, line_number - 1, i])

    if len(look_up_locations) > 1:
        chars = ""
        for location in look_up_locations:
            look_locations.append(location)
            if location[2] < 140:
                char = engine_schematic_array[location[1] - 1][1][location[2]]
                chars = chars + char

        print(chars)

    print(f"{char_left_of_number}{number}{char_right_of_number}")

    # Look down
    look_down_locations = list()
    if line_number < 140:
        for i in range(start - 1, end + 1):
            look_down_locations.append([number, line_number + 1, i])

    if len(look_down_locations) > 1:
        chars = ""
        for location in look_down_locations:
            look_locations.append(location)
            if location[2] < 140:
                char = engine_schematic_array[location[1] - 1][1][location[2]]
                chars = chars + char

        print(f"{chars}\n")

    return look_locations


part_numbers_sum = 0
line_number = 1
for engine_schematic_line in engine_schematic_array:
    line = engine_schematic_line[1]

    # Print the line above this line in the schematic
    if line_number > 1:
        print(f"{engine_schematic_array[line_number - 2][1]}")

    # Print this line in the schematic
    print(f"{line}")

    # Print the line after this line in the schematic
    if line_number < 140:
        print(f"{engine_schematic_array[line_number][1]}")
    for symbol in symbols:
        line = line.replace(symbol, " ")
    line = line.replace(".", " ")

    splits = line.split(" ")
    numbers = list()
    for split in splits:
        if split.isdigit():
            numbers.append(split)

    end = 0
    for number in numbers:
        # Keep track of the location and size of each number in the schematic
        # as we scan from left to right to find the number
        start = line.find(number, end)
        end = start + len(number)
        look_locations = where_to_look(number, line_number, start, end)
        if is_part_number(look_locations):
            part_numbers_sum += int(number)


    line_number += 1


print(f"The sum of all part numbers is: {part_numbers_sum}")
