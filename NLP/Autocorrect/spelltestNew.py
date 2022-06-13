################ Spelling Corrector 

import re
from collections import Counter
import enchant
from data_prep import *

WORDS = {}
lines = read_data("extract_data.txt")
lines = clean_word(lines)
ONE_WORD = create_one_word(lines)
TWO_WORD = create_two_word(lines)

def min_edit_dist(str1,str2):
	return enchant.utils.levenshtein(str1, str2)

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def one_possible_word_list(possible_words):
	one_word_list = []
	for word in possible_words:
		if word in ONE_WORD:
			one_word_list.append(word)
	return one_word_list

def get_all_word_comb(word):
	if len(word) <= 6:
		possible_words = edits2(word)
	else:
		possible_words = edits1(word)
	return possible_words

def two_possible_word_list(one_word_list,prev_word,next_word):
	two_word_list = []
	for word in one_word_list:
		pref_str = prev_word + " "+word
		suff_str = word + " "+next_word
		if pref_str.strip() in TWO_WORD or suff_str.strip() in TWO_WORD:
			two_word_list.append(word)
	return two_word_list


def get_spellcheck(string):
	str_list = string.split()
	d = []
	n = len(str_list)
	for i in range(n):
		prev_word = str_list[i-1] if (i-1)>=0 else ""
		next_word = str_list[i+1] if (i+1)<n else ""
		word = str_list[i]

		if word in ONE_WORD: # correct word
			d.append(word)
		else: # misspelled word
			possible_words = get_all_word_comb(word)

			one_word_list = one_possible_word_list(possible_words)

			if len(one_word_list) == 1:
				d.append(one_word_list[0])

			elif len(one_word_list) > 1:
				two_word_list = two_possible_word_list(one_word_list,prev_word,next_word)

				if len(two_word_list) == 1:
					d.append(two_word_list[0])
				else:
					d.append(word)
			else:
				d.append(word)
	correct_string = " ".join(d)
	return correct_string

while True:
	string = input("Enter : ")
	print("After spellcheck : ",get_spellcheck(string))
			



