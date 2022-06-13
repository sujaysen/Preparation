from spellchecker import SpellChecker

spell = SpellChecker(distance=1)

spell.word_frequency.load_words(['baroda'])

while True:
	word = input("Input : ")
	print("Output : ",spell.correction(word))
