import algorithm.search as search

def main():
    list = [40, 9, 20, 93, 7, 34, 85, 91]
    key = 34
    print("%d所在位置：%d" % (key, search.sequence_search(list, key)))

if __name__ == "__main__":
    main()