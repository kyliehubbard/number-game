"""
   CISC-121 2023W

   Name:   Kylie Hubbard
   Student Number: 20294570
   Email:  21kah10@queensu.ca
   Date: 2023-02-01

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""

import time
from functions import all_odd_or_even

print("Hello! Welcome to the all even or odd program! This is an interactive program that requires you to input some integers "
      "to see if they fill out the required criteria or not.")
time.sleep(1) 
integer_list = []

major_loop = False
while not major_loop:
    to_play = input("Would you like to participate? Please type 'yes' or 'no'.\n")
    if to_play== "yes":
        print("Okay great!")
        time.sleep(1)

        break_statement = False
        while not break_statement:
            input_okay = False
            while not input_okay:
                try:
                    an_integer = (int(input("What integer would you like to add? \n")))
                    input_okay = True
                    integer_list.append(an_integer)
                except ValueError:
                    print("You must enter an integer.")
                    continue

                new_integer = (input("Would you like to add another? Please type 'yes' or 'no'. \n"))
                if new_integer == "yes":
                    continue
                elif new_integer == "no":
                    print("Okay.")
                    break_statement = True
                    major_loop = True
                    break
                else:
                    print("Please type 'yes' or 'no.'")
                    continue

        print("Your integers are: " + str(integer_list))
        print(all_odd_or_even(integer_list))

    elif to_play== "no":
        print("See you next time!")
        break

    else:
        print("Please type yes or no.")
        continue
