import string

output_file = open("words.txt", "w")

with open("quotes.txt") as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            output_file.write(word + "\n")

output_file.close()