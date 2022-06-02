import re
import spacy
nlp = spacy.load('en_core_web_sm')

def stem(word):
	for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
		if word.endswith(suffix):
			return word[:-len(suffix)]
	return word


def stemmer(phrase):
	for word in phrase:
		if stem(word):
			text = re.findall(r"^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$", word)

def make_to_base(x):
	x = str(x)
	x_list = []
	doc = nlp(x)

	for token in doc:
		lemma = token.lemma_
		x_list.append(lemma)
	return " ".join(x_list)


while True:
	word = input("Enter : ")
	print("Output : ",make_to_base(word))
