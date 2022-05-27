print("Hello, giuz!")
print("hey")


c = True
d = 'Yet another var'

e = False

class MyException(Exception):
    pass

class AnotherException(MyException):
    pass

if __name__ == "__main__":

    for cls in [MyException, AnotherException]:
        try:
            print("Exception being raised: {}".format(cls.__name__))
            raise cls
        except AnotherException as e:
            print("AnotherException")
        except MyException as e:
            print("MyException")

