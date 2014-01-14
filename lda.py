# import sys
# log = open('lda.txt','w+')

# sys.stdout = log

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/alldict.dict')
corpus = corpora.MmCorpus('/tmp/corpus.mm')
print corpus
print dir(models.ldamodel.LdaModel)
print str(models.ldamodel.LdaModel.__doc__)
# model = models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=100)
# model.save('lda.txt')
model = models.ldamodel.LdaModel.load('lda.txt')
m= model.show_topic(12,200,)
print len(m)

with open('l.txt','w+') as f:
	for x in m:
		l =str(x[0])+':'+x[1]+"\n"
		f.write(str(l))
new_doc = "Human computer interaction"
with open('try.txt','r') as f:
	new_doc = f.read()
new_vec = dictionary.doc2bow(new_doc.lower().split())
doc_lda = model[new_vec]

with open('l.txt','w+') as f:
	for x in doc_lda:
		l =str(x[0])+':'+x[1]+"\n"
		f.write(str(l))