from gensim.test.utils import get_tmpfile
from gensim.test.utils import datapath
from gensim.models import Word2Vec
from sys import argv

def save_file(filename, data):
    print("Saving...")
    with open(filename, "w+") as of:
        for k, v in data:
            of.write("{}, {}\n".format(k,v))

if(len(argv) != 3 or argv[1] != "--wordcount"):
    print("Error. Usage: %s --wordcount [num]")
    exit()
try:
    wordcount = int(argv[2])
except:
    print("Error. Usage: %s --wordcount [num]")
    exit()

model = Word2Vec.load("word2vec.model")

while(True):
    print("Skriv positive og negative ord. QQ for at forlade programmet.")
    pos_words = input("Positive ord > ")
    if "QQ" in pos_words:
        exit()
    neg_words = input("Negative ord > ")
    if "QQ" in neg_words:
        exit()
    pos_words = pos_words.split()
    neg_words = neg_words.split()
    try:
        mostsim = model.wv.most_similar(positive=pos_words, negative=neg_words, topn=wordcount)
    except:
        print("Et eller flere af ordene mangler måske i ordbogen.")
        continue

    filename = ""
    if pos_words:
        filename = "POS_"
        filename += "+".join(pos_words) + "_"
    if neg_words:
        filename += "NEG_"
        filename += "+".join(neg_words) + "_"
    filename += ".txt"
    save_file(filename, mostsim)