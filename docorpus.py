import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities


class MyCorpus(object):
	def __iter__(self):
		for line in open('mycorpus.txt'):
		# assume there's one document per line, tokens separated by whitespace
		yield dictionary.doc2bow(line.lower().split())