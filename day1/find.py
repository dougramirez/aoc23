numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

calibration_values = list()
calibration_values_sum = 0

# Open the calibration document
calibration_document = open("calibration_document.txt", "r")


def looky(text, tokens) -> list:
    founds = list()
    print(text)
    for token in tokens:
        position = text.find(token) + 1
        if position > 0:
            founds.append(position)
            print(f"token {token} was found at position {position}")
    
    return founds


for line in calibration_document:
    result = looky(line, numbers)
    print(result)
