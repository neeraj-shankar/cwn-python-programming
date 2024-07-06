##############################################################################
## Introduction to format() function in Python
##############################################################################

# Converting a Decimal number into a Binary number using the format() function
decimal_number = 10
binary_result = format(decimal_number, 'b')
print('**'*50)
print(f"Corresponding Binary Value: {binary_result}")

##############################################################################
## Format of format specifier (format_spec)
## Syntax: Format: [[fill]align][sign][#][0][width][,][.precision][type]

## fill: (any character): padding character
## align: "<": left-alignment specifier ">": right-alignment specifier
## "^": center-alignment specifier "=": justified specifier

## sign: "+": Positive numbers have a "+" sign
## "-": Negative numbers have a "-" sign.
## " " (space): Positive numbers are preceded by a space
