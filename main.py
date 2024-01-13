# ########################
# Your comment header here
# ########################

# Consants. Use these in your formulas
FREEZING_F = 32.0        # freezing point of water in Fahrenheit
MULTIPLIER_F = .5555556  # this is 5/9
MULTIPLIER_C = 1.8       # this is 9/5

# this defines fahrenheit_to_celsius, but it does not run it
def fahrenheit_to_celsius(f):

    # REPLACE THIS next line with the appropriate calculation
    # Use the constants provided above.
    c = 0

    return c

# this defines celsius_to_fahrenheit, but it does not run it
def celsius_to_fahrenheit(c):

    # REPLACE THIS next line with the appropriate calculation
    # Use the constants provided above.
    f = 0

    return f

# this defines main, but it does not run it
def main():
    #ask the user for a choice, 1, 2
    choice = input("Enter\n  1 C to F\n  2 F to C\n")

    if choice == "1":
        # choice is 1, ask for and convert celsius_to_fahrenheit
        celsius = input("Enter a celsius temperature: ")
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)

        # FILL IN THIS print line to print the results appropriately
        # to match the examples given in the instructions
        print()

    elif choice == "2":
        # choice is 2, ask for and convert fahrenheit_to_celsius
        fahrenheit = input("Enter a fahrenheit temperature: ")
        fahrenheit = float(fahrenheit)
        celsius = fahrenheit_to_celsius(fahrenheit)

        # FILL IN THIS print line to print the results appropriately
        # to match the examples given in the instructions
        print()

    else:
        print("bye")

# this runs main. i.e. calls main
main()

