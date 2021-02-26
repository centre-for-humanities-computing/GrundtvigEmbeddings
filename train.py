from gensim.test.utils import get_tmpfile
from gensim.test.utils import datapath
from gensim.models import Word2Vec
import string

path = get_tmpfile("word2vec.model")

input = open("../data.txt")


class WordTrainer(object):
    def __init__(self, datastream):
        self.datastream = datastream
        self.processedFiles = 0
    def __iter__(self):
        table = str.maketrans(dict.fromkeys(string.punctuation))
        for item in self.datastream.readlines():
            #Tokenize the text
            words = item.split()
            for i in range(len(words)):
                words[i] = words[i].translate(table)
            self.processedFiles += 1
            if self.processedFiles % 10000 == 0:
                print(self.processedFiles)
            yield words

document = WordTrainer(input)

model = Word2Vec(document, min_count=1, sg=1)
model.save("word2vec.model")