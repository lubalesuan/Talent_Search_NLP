import spacy
import en_core_web_lg



nlp = en_core_web_lg.load()


def get_ents(string):
	"""
	param: array of strings
	dispatch pr
	"""

	doc = nlp(unicode(string))
	for ent in doc.ents:
		print(ent.text, ent.label_)

	print([(token.text, token.tag_) for token in doc])