def get_score_info(name, **kwargs):
    info = "[%s]\n" % name
    for subject, score in kwargs.items():
        info += "%s: %d\n" % (subject, score)
    info += "Average: %.2f" % (sum(kwargs.values()) / len(kwargs))

    return info

def main():
    print(get_score_info("Alice", Python=85, Math=80))
    print(get_score_info("Bob", Java=77, Math=82))

if __name__ == "__main__":
    main()