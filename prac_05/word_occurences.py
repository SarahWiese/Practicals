"""Program to count occurrences of words in a string."""
sentence = str(input("Enter sentence: ")).split()
sentence_dict = {}
for word in sentence:
    if word in sentence_dict:
        sentence_dict[word] += 1
    else:
        sentence_dict[word] = 1
print(sentence_dict)