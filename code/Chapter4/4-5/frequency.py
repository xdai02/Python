import string

text = """John sat on the park bench,
eating his sandwich and enjoying the warm sun on his face.
He watched the children playing and the ducks swimming in the pond,
feeling content and at peace.
"""

words = text.split()
frequency = {}

for word in words:
    word = word.lower().strip(string.punctuation)

    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

for word, count in frequency.items():
    print("%s: %d" % (word, count))