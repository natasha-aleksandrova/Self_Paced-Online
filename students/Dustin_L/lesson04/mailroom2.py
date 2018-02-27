#!/usr/bin/env python3
"""Mail Room 2 Module

This module contains all of the functions for the updated Mail Room 2 module.
"""

from collections import defaultdict
import datetime

THANK_YOU_FMT = ('\nDear {:s},\n'
                 'Thank you for your generous donation of ${:.2f}.\n'
                 '\t\tSincerely,\n'
                 '\t\t  -Your conscience')
SELECT_PROMPT = ('\nPlease select from the following options:\n'
                 '\t1. Send a Thank You\n'
                 '\t2. Create a Report\n'
                 '\t3. Send letters to all donors\n'
                 '\t4. quit\n'
                 ' --> ')
PROMPT_OPTS = (1, 2, 3, 4)
GIFTS_KEY = 'gifts'
NUM_GIFTS_KEY = 'number_of_gifts'
TOTAL_KEY = 'total'
AVE_KEY = 'average'


def init_donor_data(gifts=None):
    """Initialize each donor in the database.

        gifts (list, optional): Defaults to None. Initial donations.
    """
    if not gifts:
        gifts = []

    return {GIFTS_KEY: gifts,
            NUM_GIFTS_KEY: len(gifts),
            TOTAL_KEY: sum(gifts),
            AVE_KEY: sum(gifts) / len(gifts) if gifts else 0}


donor_db = defaultdict(lambda: init_donor_data(),
                       {'Toni Morrison': init_donor_data([1000, 5000, 10000]),
                        'Mike McHargue': init_donor_data([12000, 5000, 27000]),
                        "Flannery O'Connor": init_donor_data([38734, 6273, 67520]),
                        'Angela Davis': init_donor_data([74846, 38470, 7570, 50]),
                        'Bell Hooks': init_donor_data([634547, 47498, 474729, 4567])})


def get_usr_input():
    """Get input from user.

    Prompt user to select one of three choices. If the user selects one of
    these three, that value is returned. If not, the user is prompted again to
    select.

    Returns:
        int: Value corresponding to user choice
    """
    usr_in = int(input(SELECT_PROMPT))

    while usr_in not in PROMPT_OPTS:
        usr_in = int(
            input(f'\nPlease try again. Valid options are: {PROMPT_OPTS}'))

    return usr_in


def add_donation(donor, amount):
    """Add a new donation to the donation database.

    Args:
        donor (str): Name of donor in donation database.
        amount (int): Amount to add to donation database.
    """
    donor_db[donor][GIFTS_KEY].append(amount)
    donor_db[donor][NUM_GIFTS_KEY] += 1
    donor_db[donor][TOTAL_KEY] += amount
    donor_db[donor][AVE_KEY] = donor_db[donor][TOTAL_KEY] / \
        donor_db[donor][NUM_GIFTS_KEY]


def send_thank_you():
    """Send a thank you.

    Prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data
    structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to
    crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.
    """
    name_prompt = '\nPlease enter name of "Thank You" recipient:\n'\
                  '(Enter "list" to see all donors)\n'\
                  '(Enter "quit" to return to main menu)\n'\
                  ' --> '
    amount_prompt = '\nPlease enter the donation amount:\n'\
                    '(Enter "quit" to return to main menu)\n'\
                    ' --> '
    names = [donor.lower() for donor in donor_db]

    while True:
        usr_in = input(name_prompt).strip().lower()

        if usr_in.startswith('q'):
            break
        elif usr_in == 'list':
            print()
            for name in names:
                print(name.title())
        else:
            donor = " ".join([name.title() for name in usr_in.split()])
            usr_in = input(amount_prompt).strip().lower()

            if usr_in.startswith('q'):
                break
            else:
                donation = float(usr_in)

            add_donation(donor, donation)
            print(THANK_YOU_FMT.format(donor, donation))
            break


def create_report():
    """Generate and print a report of donors in the database

    Prints a list of donors, sorted by total historical donation amount.
    Includes Donor Name, total donated, number of donations and average
    donation
    """
    min_width = 12
    def_space = 5
    col_sep = ' | '

    max_name = len(max([dnr for dnr in donor_db], key=len)) + def_space
    max_total = len(max([str(val[TOTAL_KEY])
                         for val in donor_db.values()], key=len)) + def_space
    max_gifts = len(max([str(val[NUM_GIFTS_KEY])
                         for val in donor_db.values()], key=len)) + def_space
    max_ave = max_total

    if max_name < min_width:
        max_name = min_width
    if max_total < min_width:
        max_total = max_ave = min_width
    if max_gifts < min_width:
        max_gifts = min_width

    header = (f'\n{{:^{max_name}s}}{col_sep}{{:^{max_total}s}}{col_sep}'
              f'{{:^{max_gifts}s}}{col_sep}{{:^{max_ave}s}}\n')
    header += '-' * (max_name + max_total + max_gifts +
                     max_ave + len(col_sep) * 3)
    header = header.format('Donor Name', 'Total Given',
                           'Num Gifts', 'Average Gift')
    row_fmt = (f'{{:<{max_name}s}}{col_sep}${{:>{max_total - 1}.2f}}{col_sep}'
               f'{{:>{max_gifts}d}}{col_sep}${{:>{max_ave - 1}.2f}}')

    sorted_dnr_keys = sorted(
        donor_db, key=lambda dnr: donor_db[dnr][TOTAL_KEY], reverse=True)

    print(header)
    for dnr in sorted_dnr_keys:
        print(row_fmt.format(dnr, donor_db[dnr][TOTAL_KEY],
                             donor_db[dnr][NUM_GIFTS_KEY],
                             donor_db[dnr][AVE_KEY]))


def quit_mailroom():
    """Exit operations when quitting mail room"""
    print('Quitting mailroom...')


def send_letters():
    """Create a letter for each donor and write to disk as a text file"""
    now = datetime.datetime.today().strftime('%m-%d-%Y')

    for donor, data in donor_db.items():
        f_name = f'{donor.replace(" ", "_")}_{now}.txt'
        with open(f_name, 'w') as f:
            f.write(THANK_YOU_FMT.format(donor, data[TOTAL_KEY]))


def main():
    """Main function"""
    opt_dict = dict(zip(PROMPT_OPTS, (send_thank_you, create_report,
                                      send_letters, quit_mailroom)))
    choice = ''
    while choice != PROMPT_OPTS[-1]:
        choice = get_usr_input()
        opt_dict.get(choice)()


if __name__ == '__main__':
    main()
