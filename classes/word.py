import re
from typing import List
from operator import itemgetter
from sklearn.feature_extraction.text import CountVectorizer


class Word:
    def __init__(self) -> None:
        # texto dos tweets
        self.tweets_text = []
        # tweets pré-processados
        self.tweets_pprocessed = []
        # dicionário de frequencia das palavras
        self.word_frequencies = {}

    def pre_processing(self, tweets_collection: List):
        self.tweets_text = [tweet['full_text'] for tweet in tweets_collection]
        for text in self.tweets_text:
            # remover links
            text = re.sub("http\S+", "", text)
            # remover mentions
            text = re.sub("@\S+", "", text)
            # remover hashtags
            text = re.sub("#\S+", " ", text)
            # remover quebra de linhas
            text = re.sub("\n", " ", text)
            # remover pontuações
            text = re.sub("[^\w\s]", " ", text)
            # remover números
            # text = re.sub("[0-9]+(\s|\w)", "", text)
            # remover espaços duplos
            text = re.sub("\s{2,}", " ", text)
            # remover espaços no inicio e fim da string
            text = re.sub("^\s|\s$", "", text)
            # converter todas as letras para minusculas
            text = text.lower()
            # remover stpwords
            with open('data/stopwords.txt', 'r') as file:
                stopwords = file.readlines()
            stopwords = [sw.replace('\n','') for sw in stopwords]
            text = " ".join([i for i in text.split() if not i in stopwords])

            self.tweets_pprocessed.append(text)

    def get_word_frequencies(self):
        cvectorizer = CountVectorizer()
        cvectorizer_fit = cvectorizer.fit_transform(self.tweets_pprocessed)

        vocabulary = cvectorizer.vocabulary_
        sorted_vocabulary = sorted(
            vocabulary.items(), key=itemgetter(1), reverse=False)

        frequecies = cvectorizer_fit.toarray().sum(axis=0)

        self.word_frequencies = {
            k: int(frequecies[v]) for k, v in sorted_vocabulary}
