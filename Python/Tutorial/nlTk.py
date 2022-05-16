import nltk
from rake_nltk import Rake

#nltk.download('stopwords')
#nltk.download('punkt')
r = Rake()

def get_keyword(my_text):
	r.extract_keywords_from_text(my_text)
	keywordList           = []
	rankedList            = r.get_ranked_phrases_with_scores()
	for keyword in rankedList:
		keyword_updated       = keyword[1].split()
		keyword_updated_string    = " ".join(keyword_updated[:2])
		keywordList.append(keyword_updated_string)
		if(len(keywordList)>9):
			break
	return keywordList

for text in open("tests.txt","r"):
	resp = get_keyword(text.replace("\n",""))
	if len(resp)>0:
		print("{} ----->>>>>> {}".format(text,resp[0]))

text = input("Enter string : ")
resp = get_keyword(text)
print("Search text : ",resp[0])
