"""Program to count occurrences of words in a string and return list of words with their count."""


def main():
    """Program to count occurrences of words in a string."""
    sentence = input("Enter sentence: ").split()
    sentence.sort()
    sentence_dict = {}
    for word in sentence:
        if word in sentence_dict:
            sentence_dict[word] += 1
        else:
            sentence_dict[word] = 1
    for word, count in sentence_dict.items():
        max_length = max((len(word) for word in sentence))
        print("{:{}} : {}".format(word, max_length, count))


main()
