#!/usr/bin/env python3

# Data
donors_amts = [['Gates', 'Mr.', 150000, 3], ['Brin', 'Mr.', 150000, 3],
              ['Cerf', 'Mr.', 50000, 2], ['Musk', 'Mr.', 100000, 1],
              ['Berners-Lee', 'Mr.', 50000, 2],
              ['Wojcicki', 'Ms.', 125000, 1], ['Avey', 'Ms.', 200000, 2]]


# Processing
def send_ty():
	global donors_amts
	donors = []
	salutation = ''
	while True:
		print()
		response = input('Enter full last name of Donor,'
			+ '\n"list" for List of Donors'
			+ ',\nor "e" to Exit back to Main Menu: ')
		print()
		if response == 'e':
			break	
		if response.isalpha():
			if response == 'list':
				print('Here is the list of Donors: ')
				donors_amts.sort()
				for donor in donors_amts:
					print(donor[0])
			elif response != 'list':
				response = response.capitalize()
				for donor in donors_amts:
					donors.append(donor[0])
				if response in donors:
					print('Donor found:', response)
					new_response = int(input('Enter a Donation amount' +
						' (in USD): '))
					for donor in donors_amts:
						if donor[0] == response:
							donor[2] += new_response
							donor[3] += 1
							salutation = donor[1]
					print('Added to', response, '\'s Donations:',
						new_response, '\n')
				elif response not in donors:
					salutation = input('Salutation: "Ms." or "Mr."?: ')
					new_response = int(input('Enter a Donation amount' +
						' (in USD): '))
					print('Added to list of Donors:', salutation,
						response, new_response)
					donors_amts.append([response, salutation,
						new_response, 1])
				form_st = 'Dear {} {}, Thank you for your generous donation in the amount of {} USD.'
				print(form_st.format(salutation,
					response, new_response))


def get_report():
	# print('Here is the full List:')
	# donors_amts.sort()
	# for donor in donors_amts:
	# 	print(donor, '\n')
	print()
	psv = ['Donor Name', '| Total Given', '| Num Gifts',
	'| Average Gift']
	print('{:<15}{:>12}{:>12}{:>12}'.format(psv[0], psv[1],
		psv[2], psv[3]))
	for i in range(55):
		print('-', end='')
	print()
	for donor in donors_amts:
		print('{:<15}{}{:>10}{:>12}{}{:>11}'.format(donor[0], '  $',
			donor[2], donor[3], '  $', donor[2] // donor[3]))
	print()


# I/O
if __name__ == '__main__':
    while True:
        print('Main Menu:')
        response = input('Choose from the following:\n"1" - Send a "Thank You",'
            + '\n"2" - Create a Report, or\n"q" to Quit: ')
        if response == '1':
            send_ty()
        elif response == '2':
            get_report()
        elif response == 'q':
            print('Program execution completed.')
            break
        else:
            response = input('Choose "1", "2", or "q": ')
            if response == '1' or response == '2':
                continue
            elif response == 'q':
                print('Program execution completed.')
                break
            else:
                print('That is not an option. Closing program.')
                break

else:
    print('This module is not intended to be imported.')
