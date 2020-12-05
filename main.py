import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from classes.user import User
from classes.word import Word


def main():
    user = User(screen_name="@gean_dreson")
    user.get_tweets()

    words = Word()
    words.pre_processing(tweets_collection=user.tweets_collection)
    words.get_word_frequencies()

    with open('data/tweets.json', 'w') as file:
        json.dump(user.tweets_collection, file, indent=3, ensure_ascii=False)

    with open('data/word_frequencies.json', 'w') as file:
        json.dump(words.word_frequencies, file, indent=3, ensure_ascii=False)

    wordcloud = WordCloud(
        max_words=4000).generate_from_frequencies(words.word_frequencies)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
