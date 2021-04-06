class Person:
    def __init__(self):
        print("构造方法被执行了")
    
    def __del__(self):
        print("析构方法被执行了")

def main():
    person = Person()
    del person

if __name__ == "__main__":
    main()