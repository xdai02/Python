class Person:
    name = ""
    age = 0
    gender = ""

    def eat(self):
        print("吃饭")
    
    def sleep(self):
        print("睡觉")

def main():
    person = Person()
    
    person.name = "小灰"
    person.age = 16
    person.gender = "男"
    
    print("姓名：%s，年龄：%d，性别：%s" % (
            person.name, person.age, person.gender))
    person.eat()
    person.sleep()

if __name__ == "__main__":
    main()