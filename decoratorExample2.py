def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


star(percent(printer))
func=percent(printer)
**************
%%%%%%%%%%%%%%
hello
%%%%%%%%%%%%%%
**************

stack ---> added 5
percent is executed
stack 5,13
func =printer
printer is executed
13 will be popped out
5 will be popped







printer("Hello")
