#!usr/bin/env python3

def get_age():
    try:
        age = int(input("Age: "))
        print("Age: ",age)
    except:
        print("age is not integer")
def helloWorld():
    print("hello world")

if __name__ == "__main__":
    get_age()