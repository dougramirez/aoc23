calibration_values = list()
calibration_values_sum = 0

# Open the calibration document
calibration_document = open("calibration_document.txt", "r")

# Read each line from the calibration document
for line in calibration_document:
    print(line.find("one"))
    if "one" in line:
        print(f"we found a 'one'")



    # Inspect each character in the line
    first_digit_found = False
    for char in line:
        if char.isdigit():
            if first_digit_found == False:    
                # When the first number is found create a 2 digit calibration 
                # value using the first digit
                first_digit = char
                first_digit_found = True

            # If another number is found replace the second digit of the 
            # calibration value with the number
            second_digit = char    
    
    # After all the characters of the line from the calibration document have 
    # been inspected add the 2 digit calibration value to a list
    calibration_value = int(f"{first_digit}{second_digit}")
    print(f"calibration value is {calibration_value}")
    calibration_values.append(calibration_value)

# After all lines from the calibration document have been processed create a 
# sum of all the calibration values
for value in calibration_values:
    calibration_values_sum += value

print(calibration_values_sum)