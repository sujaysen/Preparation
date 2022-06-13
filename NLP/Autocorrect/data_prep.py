def create_one_word(lines):
	ONE_WORD = set()
	for line in lines:
		for word in line.split():
			ONE_WORD.add(word)
	return ONE_WORD

def create_two_word(lines):
	TWO_WORD = set()
	for line in lines:
		words = line.split()
		length = len(words)
		for i in range(length):
			if i+1 < length:
				TWO_WORD.add(words[i]+" "+words[i+1])
	return TWO_WORD

def clean_word(lines,considered_word_len = 4):
	docs = []
	for line in lines:
		word_list = []
		words = line.split()
		for word in words:
			if len(word) >= considered_word_len and not word.isdigit():
				word_list.append(word)
		update_line = " ".join(word_list)
		docs.append(update_line.strip())
	return docs

def read_data(filename):
	with open(filename,"r") as f:
		lines = [line.strip() for line in f]
	return lines

def write_data(data,filename):
	f = open(filename,"w")
	
lines = read_data("extract_data.txt")
lines = clean_word(lines)
ONE_WORD = create_one_word(lines)
TWO_WORD = create_two_word(lines)
f = open("one_word.txt","w")
f.write(str(ONE_WORD))
