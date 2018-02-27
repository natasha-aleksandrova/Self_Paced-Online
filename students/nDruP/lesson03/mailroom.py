#!/usr/bin/env python3
"""
1. Create Data structure that holds Donor, Donation Amount.
2. Prompt user to Send a Thank You, Create a Report, or quit.
3. At any point, the user should be able to quit their current task and return
to the original prompt
4. From the original prompt, the user should be able to quit the scipt cleanly
"""


import sys


def send_thanks():
    """
    Prompt for a full name.
    Prompt->"list": show a list of the donor names
    Prompt->name not in list: add name to list;
    Then prompt for donation amount, add amount to donation history
    Compose and print an email thanking the donor for their donation.
    Return to main
    """
    donor_name = "list"
    donation_amt = None
    print("Let's craft a very personal thank you note for our donor!")
    print("Return to the main menu at any time by entering 'exit'")
    print("Pull up a list of donor names by entering 'list'")
    while donor_name == "list":
        donor_name = input("Enter Donor Name >")
        if donor_name.lower() == "list":
            print(("{}\n"*len(name_list)).format(*name_list))
        elif donor_name.lower() == "exit":
            return
    while not donation_amt:
        donation_amt = input("Enter their Donation Amount >")
        if donation_amt.lower() == "exit":
            return
    donation_amt = float(donation_amt)
    if donor_name not in name_list:
        donor_list.append([donor_name, [donation_amt]])
    else:
        donor_list[name_list.index(donor_name)][1].append(donation_amt)
    print_divider()
    message = f"Dearest {donor_name},\n"
    message += f"Thank you so much for your donation of ${donation_amt:.2f}!\n"
    message += "We will use this for something wonderful. Something...\n"
    message += "Fantastic\n"
    message += "Shrek was supposed to have 5 movies. We're going to make that"
    message += " a reality."
    message += f"\nSincerely,\n We're a Pyramid Scheme and so is {donor_name}"
    print(message)
    return


def create_report():
    """
    Print a list of donors sorted by total historical donation amount.
    Donor Name, Total Given, Num Gifts, Average Gift
    """
    donation_list = list(enumerate([x[1] for x in donor_list]))
    donation_list = sorted(donation_list, key=sum_2ple_2, reverse=True)
    name_col_len = max([len(x) for x in name_list])
    money_col_len = 12
    headers = ["Donor Name", "Total Given", "# of Gifts", "Avg Donation"]
    cols = "{:<" + f"{name_col_len}" + "}\t|{:^" + f"{money_col_len+5}"
    cols += "}|{:^10}|{:^" + f"{money_col_len+5}" + "}"
    cols = cols.format(*headers)
    print(cols)
    print("-"*len(cols))
    for index, donation in donation_list:
        name = name_list[index]
        total = sum(donation)
        num_gift = len(donation)
        average = total/num_gift
        row = f"{name:<{name_col_len}}\t| ${total:>{money_col_len+3}.2f}|"
        row += f"{num_gift:^10d}| ${average:>{money_col_len+3}.2f}"
        print(row)
    return


def sum_2ple_2(tuples):
    """
    Sum of a 2-ple's second element
    """
    return sum(tuples[1])


def print_divider():
    """
    Prints a divider so user has better idea of when they enter a new screen.
    """
    print("\n"+"*"*50+"\n")


def main_menu():
    user_prompt = None
    valid_prompts = ["1", "2", "3"]
    while user_prompt not in valid_prompts:
        print("Please choose from the following options (1,2,3): ")
        print("1. Send a Thank you")
        print("2. Create Donor Report")
        print("3. Quit")
        user_prompt = input(">")
    return int(user_prompt)


donor_list = [["Sleve McDichael", [86457.89, 2346.43, 9099.09]],
              ["Willie Dustice", [505.05, 43.21]],
              ["Rey McScriff", [666.00]],
              ["Mike Truk", [70935.30, 12546.70, 312.00]],
              ["Bobson Dugnutt", [1234.56, 789.00]],
              ["Todd Bonzalez", [715867.83, 10352.07]]]
name_list = [x[0] for x in donor_list]
option = 0

print_divider()
print("We're a Pyramid Scheme and So Are You! E-Mailroom")
while option != 3:
    name_list = [x[0] for x in donor_list]
    print_divider()
    option = main_menu()
    if option == 1:
        print_divider()
        send_thanks()
    elif option == 2:
        print_divider()
        create_report()
print_divider()
sys.exit()
