import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


import sys, os, codecs

from gensim import corpora, models, similarities, utils

def iter_documents(top_directory):
	"""Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
	for root, dirs, files in os.walk(top_directory):
		for fil in filter(lambda fil: fil.endswith('.txt'), files):
			document = open(os.path.join(root, fil)).read() # read the entire document, as one big string
			yield utils.tokenize(document, lower=True) # or whatever tokenization suits you

class MyCorpus(object):
	def __init__(self,pathm):
		self.path = pathm
		self.dictionary = corpora.Dictionary(iter_documents(self.path))
		self.dictionary.filter_extremes(no_below=1) # check API docs for pruning params	
		self.dictionary.save('/tmp/alldict.dict')
	def __iter__(self):
		#get all file in sub directorys
		listOfallfiles=[]
		for pathn, subdirs, files in os.walk(self.path):
			for name in files:
				# print name ,pathn,subdirs
				a= pathn+'/'+name
				# print a
				listOfallfiles.append(a)
				#for each file read line by line and add to doc2bow
		

		for f in listOfallfiles:
			if not os.path.isdir(f):
				# corpus = [dictionary.doc2bow(text.split()) for text in codecs.open(f,'r','utf-8')]
				# corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)
				for line in open(f) :
					# assume there's one document per line, tokens separated by whitespace
					yield self.dictionary.doc2bow(line.split())


if __name__ == '__main__':
	# dictionary = corpora.Dictionary(line.lower().split() for line in open('docheb.txt'))
	# dictionary.save('/tmp/deerwester.dict')
	# print dictionary
	# print dictionary.token2id
	# corpus = [dictionary.doc2bow(text.split(),True,) for text in open('docheb.txt')]
	# corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)	
	m = MyCorpus('/home/sem/chayadocs/')
	corpora.MmCorpus.serialize('/tmp/corpus.mm', m)