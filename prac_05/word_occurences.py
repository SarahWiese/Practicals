"""Program to count occurrences of words in a string and return list of words with their count."""


def main():
    """Program to count occurrences of words in a string."""
    sentence = str(input("Enter sentence: ")).split()
    sentence.sort()
    sentence_dict = {}
    for word in sentence:
        if word in sentence_dict:
            sentence_dict[word] += 1
        else:
            sentence_dict[word] = 1
    for word, count in sentence_dict.items():
        print("{:{}} : {}".format(word, max_length_word(sentence), count))


def max_length_word(sentence):
    """Find longest word in sentence."""
    longest_word = 0
    for words in sentence:
        if len(words) > longest_word:
            longest_word = len(words)
            print(longest_word)
        return longest_word


main()
