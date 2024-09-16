word= input()
reversed_word = ''
for word_one in range(len(word) - 1, -1, -1):
    reversed_word += word[word_one]
print(reversed_word)
