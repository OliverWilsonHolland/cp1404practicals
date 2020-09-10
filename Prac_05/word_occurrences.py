"""
CP1404/CP5632 Practical
word occurrences program
"""
text = str(input("Text: "))
word_to_count = {}
longest_name = 0
for word in text.split(" "):
    if word in word_to_count:
        word_to_count[word] += 1
    elif len(word) > longest_name:
        longest_name = len(word)
        word_to_count[word] = 1
    elif word not in word_to_count:
        word_to_count[word] = 1
for key, value in sorted(word_to_count.items()):
    print("{:{}} : {}".format(key, longest_name, value))
