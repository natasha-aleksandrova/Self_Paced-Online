#!/usr/bin/env python3
import sys
from collections import defaultdict

donors = defaultdict(list, {'Andy': [10.00], 'Bill': [15.00, 25.00], 'Chuck': [20.00, 30.00, 40.00]})


def menu_selection(prompt, dispatch_dict):
    '''Creates a menu that accepts user input and then selects a function based on that input'''
    while True:
        try:
            response = input(prompt)
            dispatch_dict[response]()
        except KeyError:
            print('Please enter a valid selection from the menu')


def donor_list():
    '''This function creates a string with the current donor names from the dictionary'''
    donor_list = []
    for names in donors:
        donor_list.append(names)
    return "\n".join(donor_list)


def thank_you():
    '''Accepts user input, and then adds donors / donations to the donor dictionary.
    It also prints a thank you message for the latest donation'''
    print('Please enter the donor name\n (Type "list" for a list of current donor names)\n '
          'Press "q" to return to console')
    new_donor = input(':')

    if new_donor.lower() == 'list':
        print(donor_list())

    elif new_donor.lower() == 'q':
        return

    else:
        try:
            amount = float(input('Please enter the donation amount:'))
            donors[new_donor].append(amount)
            print('Thank you {} for your generous donation of ${:.2f}'.format(new_donor, amount))
        except ValueError:
            print("Please enter a round number!")


def donor_report():
    '''Outputs a string that is a table of the donors and contributions'''
    print('Here is a list of donors and contributions')
    report = []
    report.append('|{:<20}|{:<20}|{:<20}|{:<20}|'.format('Name', 'Total', 'Donations', 'Average'))
    for donor_names, donor_data in donors.items():
        total_donation = int(sum(donor_data))
        avg_don = len(donor_data)
        report.append('|{:<20}|{:>20}|{:>20}|{:>20}|'.format(donor_names, total_donation, avg_don, total_donation / avg_don))
    return '\n'.join(report)

def batch_file():
    '''Creates a text file with a thank you message for each of the donors in the dictionary'''
    for donor_data in donors:
        filename = donor_data.replace(" ", "_") + ".txt"
        total_donation = sum(donors[donor_data])
        letter = ('Thank you {} for you generous contributions totalling {:.2f}!'.format(donor_data, total_donation))
        with open(filename, 'w') as file:
            file.write(letter)
        print(f"{donor_data}'s letter has been saved to " + filename)


def quit_console():
    sys.exit("Exiting the program")


def print_donor_report():
    print(donor_report())

console_prompt = ("\nWelcome to the Donor Tracking System\n"
                  "Please press a number to make a selection\n"
                  "1.) Send a thank you note\n"
                  "2.) Create a Report\n"
                  "3.) Send letters to everyone!\n"
                  "4.) Quit(press 'q')\n")


console_dict = {'1': thank_you,
                '2': print_donor_report,
                '3': batch_file,
                '4': quit_console,
                'q': quit_console,
                'Q': quit_console}


if __name__ == '__main__':
    menu_selection(console_prompt, console_dict)
