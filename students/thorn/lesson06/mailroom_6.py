import os

"""
Thomas Horn
mailroom.py
Tracks donor information and automates the sending of thank you notes.
"""
donors = {
    'Tom Horn': [599.23, 1000.00],
    'Theo Hartwell': [0.01, 0.01, 0.1],
    'Bailey Kimmitt': [8723.22, 27167.22, 91817.66],
    'Paul Hubbell': [90012.32, 2312.24],
    'David Beckham': [1817266.11, 123123.66, 111335.112]
}

def get_donor_names():
    """ Returns the donor keys - representing the donor names. """
    return donors.keys()


def get_donor_totals(donor):
    """ Returns the total donation for a donor.  Not currently active. Except for testing. """
    print(sum(donors[donor]))
    return(sum(donors[donor]))


def print_thanks(name_request, donation_amount):
    message = f"""Dear {name_request},
        Thank you for you generous donation of ${donation_amount:.2f}.
        It will truly help the children.

        Sincerely,
        Donation Recievers"""
    print(message)


def send_thanks():
    """
    Prompts user for a full name and performs an action based on the input.
    - 'list' -> shows a list of donor names and re-prompts
    - Name not in list -> adds the name to the data structure and uses it
    - Name in list -> use it
    After name is used -> prompt for donation amount and turn into a number.
    - Add that amount to donation history of selected user
    - Print thank you note
    - Returns to original prompt or quit to prompt
    """
    # Exception block test -> see if they entered an actual titled name
    # Ignore the fact that it lowercases the name later
    try:
        name_request = input("Please enter a donor's full name, or 'list' for a full list of donors.  'Quit' or 'Return' valid commands. ")
        name_request[0] = name_request.title[1]
    except:
        print("Names start with an uppercase letter here.")
        name_request = name_request.title()
        
    # Return or Quit.
    if name_request.lower() == "quit":
        quit()

    if name_request.lower() == "return":
        return

    # List request - list of donors returned
    # Exception added to make user format it properly.
    if name_request.lower() == 'list':
        # print('\n'.join(get_donor_names()))
        donor_names = get_donor_names()
        print('\n'.join(donor_names))
        return

    name_request = name_request.title()
    donation_amount = float(input(("Please enter a donation amount for {}: ".format(name_request))))
    print()

    # Add to existing donor or put new donor and amount in the list.
    if name_request in donors.keys():
        donors[name_request].append(donation_amount)
        print_thanks(name_request, donation_amount)

    else:
        donors[name_request] = [donation_amount]
        print_thanks(name_request, donation_amount)

def get_report():
    print(create_report())
        
def create_report():
    """
    Prints a list of donors sorted by total historical donation amount.
    - Includes donor name, total donated, number of donations, average donation
      amount.
    - $ Total - 27 spaces in, right justified
    """
    line_out = ''
    line_out += "Donor:                    | $    Total     |   Donations   | $   Average   |\n"
    line_out += ("-"*76) + '\n'
    # List is sorted by donor amounts desc.  Create preset list to pass in 
    # vars once the list is sorted.
    line_in = "{:<26}| ${:>14,.2f}|{:>15}| ${:>13,.2f}\n"

    lines = create_report_lines()
    # Append relevant information to the list to be sorted.
 

    for donor_set in lines:
        # print(line_in.format(*donor_set))
        line_out += line_in.format(*donor_set)

    return line_out


def create_report_lines():
    i = 0
    lines = [[] for _ in range(len(donors.keys()))]

    for name, donation in donors.items():
        try:
            lines[i].append(name)
            lines[i].append(sum(donation))
            lines[i].append(len(donation))
            lines[i].append(sum(donation)/len(donation))
            i += 1
        except IndexError:
            continue
    lines.sort(key=lambda x: x[1], reverse=True)
    return lines


def send_letters():
    """ 
    Creates a letter for every donor and saves it to the root directory. 
    Letter will contain the donors name and total donation amount.
    """
    cwd = os.getcwd()
    # Get donors (donors[0]), donations (donors[1]), and write letters.
    for donor in donors.items():
        total = sum(donor[1])
        outletter = os.path.join(cwd, f'{donor[0]}_ty_letter.txt')
        with open(outletter, 'w+') as f:
            message = f"""Dear {donor[0]},
            Thank you for you generous donation of ${total:.2f}.
        It will truly help the children.


        Sincerely,
        Donation Receivers
    """
            f.write(message)


def quitter():
    print("Exiting")
    quit()

if __name__ == "__main__":
    # Select from options.
    while True:
        choice = input(
        "Please select an option:\n\
        1 - Send Thanks\n\
        2 - Create Donor Report\n\
        3 - Send Letters\n\
        4 - Quit\n")
        print()
        user_choices = {
            '1': send_thanks,
            '2': get_report,
            '3': send_letters,
            '4': quitter
        }
        try:
            user_choices[choice]()
        except KeyError:
            print("Invalid choice.")
            continue
        


