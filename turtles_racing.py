def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter valid number. Try again.")
            continue

        if 2 <= racers <=10:
            return racers
        else:
            print("Number is not in range 2 -10. Try again.")


