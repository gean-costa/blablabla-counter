import json
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


if __name__ == "__main__":
    main()
