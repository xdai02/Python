class Person:
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age

def main():
    person = Person()
    person.set_name("小灰")
    person.set_age(16)
    print("姓名：%s，年龄：%d" % (
            person.get_name(), person.get_age()))

if __name__ == "__main__":
    main()