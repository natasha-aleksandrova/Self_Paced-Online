#!/usr/bin/env python3
import random
"""
Trigram analysis: Look at each set of three adjacent words in a document.
Use the first two words of the set as a *key*, and remember the fact that
the third word followed that key. Once you’ve finished, you know the *list*
of individual words that can follow each two word sequence in the document.
For example, given the input:

I wish I may I wish I might

You might generate:

"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I"  => ["wish"]
"I may"  => ["I"]

This says that the words “I wish” are twice followed by the word “I”,
the words “wish I” are followed once by “may” and once by “might” and so on.

To generate new text from this analysis, choose an arbitrary word pair
as a starting point. Use these to look up a random next word
(using the table above) and append this new word to the text so far.
This now gives you a new word pair at the end of the text, so look up
a potential next word based on these. Add this to the list, and so on.

In this kata, what we’re experimenting with is not just the code,
but the heuristics of processing the text. What do we do with punctuation?
Paragraphs? Do we have to implement backtracking if we chose
a next word that turns out to be a dead end?
"""

# Data
# no data


# Processing
def clean_data():
    testfile_dict = {1: 'sherlock_small.txt', 2: 'sherlock.txt'}
    read_data = ''
    prompt = input('Enter "1" for short text file, '
                   + 'or "2" for longer text file: ')
    with open(testfile_dict[int(prompt)], 'r') as f:
        # header_size = 0
        read_data = f.read()
        # read_data = f.seek('To Sherlock Holmes she')
    replace_map = {'': ('\r', '"', '\'', '(', ')'), ' ': ('"\r', '"\n',
                   '.\r', '\n', '" ', '--', '-', ', ', '. ', '? ', '! ')}
    for new_char, chars in replace_map.items():
        for c in chars:
            read_data = read_data.replace(c, new_char)
    # read_data = ''.join(read_data.split('\r'))
    # read_data = ''.join(read_data.split('"'))
    # read_data = ' '.join(read_data.split('\n'))
    # read_data = ' '.join(read_data.split('--'))
    # read_data = ' '.join(read_data.split('-'))
    # read_data = ' '.join(read_data.split(', '))
    # read_data = ' '.join(read_data.split('. '))
    # read_data = ''.join(read_data.split('('))
    # read_data = ''.join(read_data.split(')'))
    read_data = read_data.strip('.')
    read_data = read_data.strip('  ')
    read_data_list = read_data.split(' ')

    if len(read_data_list) < 200:
        print(read_data_list)
    return read_data_list


def make_string_dict(lst):
    # lines between this and comment on line 86 can be encapsulated
    # into a separate fxn
    # possible name: def make_st_dict(lst):
    read_data = lst
    s1 = ''
    s2 = ''
    st_key = None
    s3 = ''
    st_dict = {}
    # count = 0
    for i, word in enumerate(read_data):
        if i + 2 < len(read_data):
            s1 = word
            s2 = read_data[i + 1]
            st_key = (s1, s2)
            s3 = read_data[i + 2]
            if st_key not in st_dict:
                st_dict[st_key] = [s3]
            else:
                st_dict[st_key] += [s3]
    # count += 1
    return st_dict
# see comment line above


def print_string_dict(st_dictionary):
    st_dict = st_dictionary
    print('\nst_dict:')
    # for k, v in st_dict.items():
    #     print(k, v, end='\n')
    print('\nProcessing...\n')
    print('len(st_dict):', len(st_dict))


def count_empty_strings(st_dictionary):
    st_dict = st_dictionary
    count = 0
    st_dict_vals = st_dict.values()
    for lst in st_dict_vals:
        if '' in lst:
            count += 1
    print('count of \'\' in st_dict:', count)


def make_new_string(st_dictionary):
    st_dict = st_dictionary
    new_st_lst = []
    rand_k = random.choice(list(st_dict))
    rand_v = random.choice(st_dict[rand_k])
    n = 0
    sentence_frame = random.randrange(8, 13)
    output = []

    new_st_lst.extend([rand_k[0], rand_k[1], rand_v])
    print('\ninitial new_st_lst:', new_st_lst)
    potential_k = (new_st_lst[-2], new_st_lst[-1])
    for i in range(len(st_dict) // 8):
        if potential_k in st_dict:
            new_st_lst.append(random.choice(st_dict[potential_k]))
        potential_k = (new_st_lst[-2], new_st_lst[-1])
        # n += 1

    print('len(new_st_lst):', len(new_st_lst))
    # print(new_st_lst)
    for i, s in enumerate(new_st_lst[:]):
        if s == '':
            continue
        elif s == 'The' or s == 'A' or s == 'An':
            s = s.lower()
            output.append(s)
        else:
            if i % sentence_frame == 2:
                output.extend([s + '.'])
                n += 1
                sentence_frame = random.randrange(8, 13)
                if n % 3 == 0:
                    output.append('\n\n')
            else:
                output.append(s)
    output_string = ' '.join(output)
    print('\nnew string:')
    print(output_string)


# I/O
cleaned_data = clean_data()
data_dict = make_string_dict(cleaned_data)
if len(data_dict) < 200:
    print_string_dict(data_dict)
count_empty_strings(data_dict)
make_new_string(data_dict)
