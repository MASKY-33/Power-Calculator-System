# Learning "try...except" inside the "while-loop" using (** "power of exponentiation")


while True:
    chosen_number = input("Give in a number: ")

    if chosen_number == "stop":
        break

    try:
        digit = int(chosen_number)
        math = 10.0 ** digit
        print(f"{math} powers of {digit}")

    except ValueError:
        print("Invalid, put in a number.")

    except OverflowError:
        print("System crash: Please put in smaller numbers.")
