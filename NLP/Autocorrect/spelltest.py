import re
from collections import Counter


with open('keyword.txt') as f:
	lines = [line.rstrip() for line in f]

keyword_list = set()
for line in lines:
	words = line.split()
	for i in range(0,len(words)):
		keyword_list.add(words[i])
		if i+1 < len(words):
			keyword_list.add(words[i]+" "+words[i+1])
WORDS = keyword_list
print(len(WORDS))

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

prev_word = ""
while True:
	for string in lines:
		#print("Given string : ",string)
		fin_string = ""
		prev_word = ""

		string_list = string.split()
		
		for word in string_list:
			if word in WORDS:
				fin_string = fin_string + " "+word
				continue
			else:
				possible_list = edits2(word)
				for w in possible_list:
					if w in WORDS:
						fin_string = fin_string + " "+w
						break
				prev_word = word
				
		if string != fin_string.strip():
			print(string)
			print("Output : ",fin_string.strip())
