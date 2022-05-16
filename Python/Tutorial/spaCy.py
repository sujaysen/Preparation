import spacy
from collections import Counter
from string import punctuation
nlp = spacy.load("en_core_web_sm")
#nlp.Defaults.stop_words.add("my_new_stopword")
#nlp.Defaults.stop_words.remove("whatever")

def get_keywords(text):
	result = []
	pos_tag = ['PROPN', 'NOUN'] 
	doc = nlp(text.lower()) 
	for token in doc:
		print(token,token.pos_)
		if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
			continue
		if(token.pos_ in pos_tag):
			result.append(token.text)
	return result

new_text = input("Enter string : ")
output = set(get_keywords(new_text))
most_common_list = Counter(output).most_common(10)
print(most_common_list)
for res in most_common_list:
	print("Search term : ",res[0])
