#!/usr/bin/env python3

"""
Trigram analysis: Look at each *set* of three adjacent words in a document.
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
"""

# Data
sample_st = 'I wish I may I wish I might'
s1 = ''
s2 = ''
s3 = ''
count = 0
st_set = set()
st_dict = {}
pron_set = set(['I', 'you', 'she', 'he', 'it', 'we', 'they'])


# Processing
st_split_lst = sample_st.split(' ')
print('st_split_lst: ', st_split_lst, '\n')
for i, word in enumerate(st_split_lst):
    if i + 2 < len(st_split_lst):
        s1 = word
        s2 = st_split_lst[i + 1]
        s3 = st_split_lst[i + 2]
        st_set.update([s1, s2])
        st_dict[count] = {frozenset(st_set): s3}
        # print('st_set:', st_set)
        count += 1
        s1 = ''
        s2 = ''
        s3 = ''
        st_set = set()
for k, v in st_dict.items():
    print(k, v, '\n')
