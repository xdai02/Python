import jieba

FILENAME = "西游记.txt"

def read_file(FILENAME):
    with open(file=FILENAME, mode="r", encoding="UTF-8") as file:
        return file.readlines()

def word_frequency(text, n=10):
    frequency = {}

    for line in text:
        words = jieba.lcut(line)
        for word in words:
            if len(word) == 1:
                continue
            
            frequency[word] = frequency.get(word, 0) + 1

    items = list(frequency.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]

def main():
    text = read_file(FILENAME)
    frequency = word_frequency(text, 20)
    for i, item in enumerate(frequency):
        print("No.%2d: %s - %d" % (i + 1, item[0], item[1]))
    
if __name__ == "__main__":
    main()