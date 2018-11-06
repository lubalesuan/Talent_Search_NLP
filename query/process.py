import spacy
import en_core_web_lg



nlp = en_core_web_lg.load()


def get_ents(string):
	"""
	param: array of strings
	dispatch pr
	"""

	doc = nlp(str(string))
	for chunk in doc.noun_chunks:
 	   print(chunk.text, chunk.label_, chunk.root.text)
    
	for token in doc:
		print("{0}/{1} <--{2}-- {3}/{4}".format(
    		token.text, token.tag_, token.dep_, token.head.text, token.head.tag_))